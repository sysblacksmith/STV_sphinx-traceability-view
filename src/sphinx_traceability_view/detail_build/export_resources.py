"""Output-contained, inert resource records for standalone SVG snapshots."""
import base64
import hashlib
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

SVG = "http://www.w3.org/2000/svg"
TAGS = set("svg g defs path rect circle ellipse line polyline polygon text tspan use image clipPath mask marker pattern linearGradient radialGradient stop title desc style".split())
EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".woff", ".woff2", ".ttf", ".otf"}


def collect(output, fragments=None):
    root = Path(output).resolve()
    assets, visiting = {}, set()
    inline_css = []

    def local(value, source):
        parsed = urlsplit(value)
        if parsed.scheme or parsed.netloc:
            raise ValueError("External export resource is not permitted")
        path = (source.parent / unquote(parsed.path)).resolve()
        if not path.is_relative_to(root):
            raise ValueError("Export resource escapes the output directory")
        return path, parsed.fragment

    def resource(path):
        path = path.resolve()
        if not path.is_relative_to(root):
            raise ValueError("Export resource escapes the output directory")
        name = path.relative_to(root).as_posix()
        if name in visiting:
            raise ValueError("Cyclic export resource")
        if name in assets:
            if "error" in assets[name]:
                raise ValueError(assets[name]["error"])
            return assets[name]["data"]
        visiting.add(name)
        try:
            data = path.read_bytes()
            mime = None
            for signature, kind in [(b"\x89PNG\r\n\x1a\n", "image/png"), (b"\xff\xd8\xff", "image/jpeg"),
                                    (b"GIF8", "image/gif"), (b"wOFF", "font/woff"), (b"wOF2", "font/woff2"),
                                    (b"\x00\x01\x00\x00", "font/ttf"), (b"OTTO", "font/otf")]:
                if data.startswith(signature):
                    mime = kind
                    break
            if data.startswith(b"RIFF") and data[8:12] == b"WEBP":
                mime = "image/webp"
            if path.suffix.lower() == ".svg":
                if re.search(br"<!DOCTYPE|<!ENTITY", data.replace(b'\x00', b''), re.I):
                    raise ValueError("SVG entity declarations are not permitted")
                element = ET.fromstring(data)

                def target(value):
                    if value.startswith("#"):
                        return value
                    if re.match(r"data:image/(png|jpeg|gif|webp);base64,[a-zA-Z0-9+/=]+$", value):
                        return value
                    dependency, fragment = local(value, path)
                    return resource(dependency) + ("#" + fragment if fragment else "")

                for node in element.iter():
                    if not node.tag.startswith("{" + SVG + "}") or node.tag.split("}")[-1] not in TAGS:
                        raise ValueError("Unsupported or active SVG element")
                    for key, value in list(node.attrib.items()):
                        short = key.split("}")[-1].lower()
                        if short.startswith("on") or short in ("base", "src"):
                            raise ValueError("Active SVG attribute")
                        if short == "href":
                            node.set(key, target(value))
                        elif "url(" in value.lower():
                            node.set(key, re.sub(r"url\(\s*['\"]?([^)'\"]+)['\"]?\s*\)", lambda m: 'url("' + target(m[1]) + '")', value, flags=re.I))
                    if node.tag.endswith("}style") and node.text:
                        if "@import" in node.text.lower():
                            raise ValueError("SVG CSS imports are not permitted")
                        node.text = re.sub(r"url\(\s*['\"]?([^)'\"]+)['\"]?\s*\)", lambda m: 'url("' + target(m[1]) + '")', node.text, flags=re.I)
                data = ET.tostring(element, encoding="utf-8")
                mime = "image/svg+xml"
            if mime is None:
                raise ValueError("Unrecognized export resource content")
            value = "data:" + mime + ";base64," + base64.b64encode(data).decode("ascii")
            assets[name] = {"data": value, "sha256": hashlib.sha256(data).hexdigest()}
            return value
        except (OSError, ValueError, ET.ParseError) as error:
            message = "Local export resource unavailable" if isinstance(error, OSError) else str(error)
            assets[name] = {"error": message}
            raise ValueError(message) from error
        finally:
            visiting.remove(name)

    selected = set()
    css_paths = set()
    if fragments is None:
        selected.update(p for p in root.rglob("*") if p.suffix.lower() in EXTENSIONS and p.is_file())
        css_paths.update(root.rglob("*.css"))
    else:
        def select(value, source):
            if value.startswith(('data:', '#')):
                return
            try:
                path, _ = local(value, source)
                selected.add(path)
            except ValueError:
                pass  # Remote content retains the existing offline placeholder.

        for fragment in fragments:
            soup = BeautifulSoup(fragment, 'html.parser')
            for node in soup.find_all(True):
                for attr in ('data-stv-src', 'data-stv-poster', 'data-stv-xlink-href'):
                    if node.get(attr):
                        select(node[attr], root / 'index.html')
                for match in re.finditer(r'\s*(data:[^\s]+|[^,\s]+)(?:\s+[0-9.]+[wx])?\s*(?:,|$)', node.get('data-stv-srcset', '')):
                    select(match[1].rstrip(','), root / 'index.html')
                css = node.get('data-stv-style', '') + ' ' + node.get('data-stv-css', '')
                if '@font-face' in css.lower():
                    inline_css.append((css, root / 'index.html'))
                for match in re.finditer(r'url\(\s*[\"\']?([^\"\')]+)[\"\']?\s*\)', css, re.I):
                    select(match[1], root / 'index.html')
        for page in root.rglob('*.html'):
            if not page.resolve().is_relative_to(root):
                continue
            soup = BeautifulSoup(page.read_text(encoding='utf-8'), 'html.parser')
            for link in soup.select('link[rel~=stylesheet][href]'):
                try:
                    css_path, _ = local(link['href'], page)
                    css_paths.add(css_path)
                except ValueError:
                    pass
    visited_css = set()
    while css_paths - visited_css:
        path = next(iter(css_paths - visited_css))
        visited_css.add(path)
        if not path.is_file() or not path.resolve().is_relative_to(root):
            continue
        text = path.read_text(encoding='utf-8', errors='replace')
        for match in re.finditer(r'@import\s+[\"\']([^\"\']+)[\"\']', text, re.I):
            try:
                dependency, _ = local(match[1], path)
                css_paths.add(dependency)
            except ValueError:
                pass
        for match in re.finditer(r'url\(\s*[\"\']?([^\"\')]+)[\"\']?\s*\)', text, re.I):
            try:
                dependency, _ = local(match[1], path)
                if dependency.suffix.lower() == '.css':
                    css_paths.add(dependency)
                elif dependency.suffix.lower() in EXTENSIONS:
                    selected.add(dependency)
            except ValueError:
                pass
    for path in sorted(selected):
        try:
            resource(path)
        except ValueError:
            pass  # The explicit error record makes required visible export fail.
    fonts = []
    font_sources = inline_css + [(p.read_text(encoding='utf-8', errors='replace'), p) for p in sorted(visited_css) if p.is_file() and p.resolve().is_relative_to(root)]
    for text, path in font_sources:
        for match in re.finditer(r"@font-face\s*\{([^}]+)\}", text, re.I):
            rule = match[0]
            family = re.search(r"font-family\s*:\s*([^;]+)", match[1], re.I)
            if not family:
                continue
            try:
                def replace(m):
                    dependency, _ = local(m[1].strip(' \"\''), path)
                    return 'url("' + resource(dependency) + '")'
                rewritten = re.sub(r"url\(([^)]+)\)", replace, rule, flags=re.I)
                fonts.append({"family": family[1].strip(' \"\''), "css": rewritten})
            except ValueError as error:
                fonts.append({"family": family[1].strip(' \"\''), "error": str(error)})
    return {"assets": assets, "fonts": fonts}

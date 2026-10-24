"""Extract static host markup and make local resources portable."""
from copy import copy
from html import escape
import posixpath
import re
from urllib.parse import urlsplit, urlunsplit, unquote
from bs4 import BeautifulSoup


def static_css(css, page):
    resources = []
    def url(match):
        raw = match.group(1).strip().strip('\"\'')
        target = portable_url(raw, page)
        parsed = urlsplit(target or "")
        if target and (parsed.netloc or parsed.scheme in ("http", "https")):
            resources.append(target)
            return "none"
        if not target or parsed.scheme not in ("", "data"):
            return "none"
        if parsed.scheme == "data" and not target.lower().startswith(("data:image/png", "data:image/jpeg", "data:image/gif", "data:image/webp")):
            return "none"
        return 'url("' + target.replace('"', '%22') + '")'
    def imported(match):
        targets = re.findall(r'(?:url\(\s*)?[\"\']([^\"\']+)[\"\']', match.group())
        resources.extend(target for value in targets if (target := portable_url(value, page)))
        return ""
    css = re.sub(r'@import\s+[^;]+;?', imported, css, flags=re.I)
    return re.sub(r'url\(\s*([^)]*)\)', url, css, flags=re.I), resources


def portable_url(value, page):
    parsed = urlsplit(value.strip())
    if parsed.scheme.lower() not in ("", "http", "https", "mailto", "tel", "data"):
        return None
    if parsed.scheme or parsed.netloc:
        return value
    path = posixpath.normpath(posixpath.join(posixpath.dirname(page), parsed.path)) if parsed.path else page
    if path.startswith("../") or path.startswith("/"):
        return None
    return urlunsplit(("", "", path, parsed.query, parsed.fragment))


def transform(markup, page, hidden, relation_names=()):
    soup = BeautifulSoup(markup, "html.parser")
    relation_names = set(relation_names)
    for tag in list(soup.find_all(True)):
        if tag.parent is None:
            continue
        if tag.name in ("script", "iframe", "object", "embed", "link", "base", "form", "meta"):
            source = tag.get("src") or tag.get("data") or tag.get("href")
            source = portable_url(source, page) if source else None
            if source and urlsplit(source).scheme == "data":
                source = None
            if source:
                placeholder = soup.new_tag("span")
                placeholder.string = "Embedded resource unavailable offline. "
                link = soup.new_tag("a", href=source)
                if not urlsplit(source).scheme and not urlsplit(source).netloc:
                    link["data-stv-href"] = source
                link.string = "Original resource"
                placeholder.append(link)
                tag.replace_with(placeholder)
            else:
                tag.decompose()
            continue
        if tag.name == "a" and hidden and unquote(urlsplit(tag.get("href", "")).fragment) in hidden:
            relationship_reference = any(set(parent.get("class", [])) & relation_names
                                         for parent in tag.parents if parent.name)
            if relationship_reference:
                tag.decompose()
                continue
        for attr in list(tag.attrs):
            if attr.lower().startswith("on"):
                del tag[attr]
        resources = []
        for attr in ("href", "xlink:href", "src", "poster"):
            if attr not in tag.attrs:
                continue
            value = portable_url(tag[attr], page)
            parsed = urlsplit(value or "")
            embedded = attr != "href" or tag.name != "a"
            if value is None or (parsed.scheme == "data" and not (embedded and value.lower().startswith(("data:image/png", "data:image/jpeg", "data:image/gif", "data:image/webp")))):
                del tag[attr]
            elif embedded and (parsed.netloc or parsed.scheme in ("http", "https")):
                resources.append(value)
                del tag[attr]
            else:
                tag[attr] = value
                if not parsed.scheme and not parsed.netloc:
                    tag[f"data-stv-{attr.replace(':', '-')}"] = value
        if tag.has_attr("srcset"):
            value = tag["srcset"]
            del tag["srcset"]
            sources = []
            candidates = re.finditer(r'\s*(data:[^\s]+|[^,\s]+)(?:\s+([0-9.]+[wx]))?\s*(?:,|$)', value)
            for candidate in candidates:
                url = portable_url(candidate[1].rstrip(','), page)
                descriptor = candidate[2] or ""
                permitted_data = url and url.lower().startswith(("data:image/png", "data:image/jpeg", "data:image/gif", "data:image/webp"))
                if url and ((not urlsplit(url).scheme and not urlsplit(url).netloc) or permitted_data):
                    sources.append((url + " " + descriptor).strip())
                elif url:
                    resources.append(url)
            if sources:
                tag["data-stv-srcset"] = ", ".join(sources)
        if tag.has_attr("style") or tag.name == "style":
            text = tag.get("style", "") if tag.name != "style" else tag.get_text()
            css, css_resources = static_css(text, page)
            resources.extend(css_resources)
            if tag.name == "style":
                tag.string = css
                tag["data-stv-css"] = css
            else:
                tag["style"] = css
                tag["data-stv-style"] = css
        for url in resources:
            note = soup.new_tag("span", attrs={"class": "stv-unavailable"})
            note.string = "Resource unavailable offline. "
            link = soup.new_tag("a", href=url)
            if not urlsplit(url).scheme and not urlsplit(url).netloc:
                link["data-stv-href"] = url
            link.string = "Original resource"
            note.append(link)
            tag.insert_after(note)
    return str(soup)


def extract(graph, output, hidden):
    pages = {}
    fragments = {}
    for identity, obj in graph["objects"].items():
        if obj["external"]:
            fields = "".join(f"<dt>{escape(k)}</dt><dd>{escape(str(v))}</dd>" for k, v in obj.get("metadata", obj).items() if v is not None)
            fragments[identity] = f'<div><p>External object: full body unavailable offline.</p><dl>{fields}</dl></div>'
            continue
        page = urlsplit(obj["url"]).path
        if page not in pages:
            path = (output / page).resolve()
            if not path.is_relative_to(output.resolve()):
                raise ValueError(f"Object page escapes output directory: {page}")
            soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
            pages[page] = {tag["id"]: tag for tag in soup.find_all(id=True)}
        original = pages[page].get(obj["parent"] or identity)
        if original is None:
            raise ValueError(f"Rendered Need {identity!r} missing in {page}")
        fragments[identity] = transform(str(copy(original)), page, hidden, graph["model"]["relations"])
    return fragments

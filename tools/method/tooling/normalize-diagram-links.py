"""Restore Draw.io source hyperlinks after desktop SVG export; preserve geometry."""
import argparse
import html
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET


def normalize(source, svg):
    links = {e.get('link') for e in ET.parse(source).getroot().iter() if e.get('link')}
    relative = [link for link in links if not urlsplit(link).scheme and not link.startswith('//')]
    text = svg.read_text(encoding='utf-8')

    def replace(match):
        value = html.unescape(match[2])
        if urlsplit(value).scheme != 'file':
            return match[0]
        candidates = [link for link in relative if unquote(value).endswith('/' + unquote(link).lstrip('./'))]
        if len(candidates) != 1:
            raise ValueError(f'{svg}: cannot uniquely restore exported local link {value}')
        return match[1] + html.escape(candidates[0], quote=True) + match[3]

    text = re.sub(r'((?:xlink:)?href=")(.*?)(")', replace, text)
    exported = {e.get('{http://www.w3.org/1999/xlink}href', e.get('href')) for e in ET.fromstring(text).iter()}
    missing = links - exported
    if missing:
        raise ValueError(f'{svg}: source links missing from export: {sorted(missing)}')
    if text != svg.read_text(encoding='utf-8'):
        svg.write_text(text, encoding='utf-8')
    return relative


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--diagram-dir', type=Path, required=True)
    parser.add_argument('--published-dir', type=Path, help='Published location of these SVGs; validate local target pages and anchors')
    args = parser.parse_args()
    sources = sorted(args.diagram_dir.glob('*.drawio'))
    if not sources:
        parser.error('No .drawio sources found')
    for source in sources:
        svg = source.with_suffix('.svg')
        links = normalize(source, svg)
        if args.published_dir:
            for link in links:
                parts = urlsplit(link)
                target = args.published_dir / unquote(parts.path)
                if not target.is_file():
                    raise ValueError(f'Missing published target: {target}')
                if parts.fragment:
                    content = target.read_text(encoding='utf-8')
                    if not re.search(r'\bid=[\"\x27]' + re.escape(unquote(parts.fragment)) + r'[\"\x27]', content):
                        raise ValueError(f'Missing anchor: {link}')
        print(f'{source.name}: {len(links)} portable links verified')


if __name__ == '__main__':
    main()


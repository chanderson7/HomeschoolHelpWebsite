"""Check authored static pages for missing local targets and anchors."""
from html.parser import HTMLParser
from pathlib import Path
import json
from urllib.parse import urlsplit, unquote
ROOT = Path(__file__).resolve().parents[1]
class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.ids=set()
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if 'id' in attrs: self.ids.add(attrs['id'])
        for key in ('href', 'src'):
            if key in attrs: self.links.append(attrs[key])
pages={}
for name in ('index.html','preview/index.html','privacy/index.html','support/index.html','terms/index.html','data-choices/index.html','auth/callback/index.html'):
    path=ROOT/name; parser=Links(); parser.feed(path.read_text()); pages[path]=parser
errors=[]
for path, parser in pages.items():
    for link in parser.links:
        url=urlsplit(link)
        if url.scheme or url.netloc: continue
        target=(path.parent/unquote(url.path)).resolve() if url.path else path
        if target.is_dir(): target=target/'index.html'
        if not target.exists(): errors.append(f'{path.relative_to(ROOT)}: missing {link}')
        elif url.fragment and target in pages and url.fragment not in pages[target].ids:
            errors.append(f'{path.relative_to(ROOT)}: missing anchor {link}')
assert not errors, '\n'.join(errors)
aasa=json.loads((ROOT/'.well-known/apple-app-site-association').read_text())
details=aasa.get('applinks', {}).get('details', [])
assert any('26BWL2RFDX.com.chanderson7.HomeSchoolHelper' in item.get('appIDs', []) for item in details), 'AASA app identifier is missing'
assert any(any(component.get('/') == '/auth/*' for component in item.get('components', [])) for item in details), 'AASA auth callback path is missing'
print(f'PASS: local links and anchors on {len(pages)} pages; AASA association')

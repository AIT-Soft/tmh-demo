import re
import pathlib

s = pathlib.Path(__file__).parent.parent / "site"
h = (s / "index.html").read_text(encoding="utf-8")
js = (s / "assets/js/main.js").read_text(encoding="utf-8")
assert h.count("<h1") == 1
for k in ['lang="vi"', "<title>", 'name="description"', 'og:title', 'og:description', 'og:type',
          'og:locale', 'content="noindex"', 'rel="icon"', 'aria-expanded="false"',
          'aria-current="page"', 'skip-link', 'không phải phòng khám thật']:
    assert k in h, k
assert not re.search(r'(src|href)="https?:', h)
for ref in re.findall(r'(?:src|href)="(assets/[^"]+)"', h):
    assert (s / ref).exists(), ref
assert len(js.encode()) <= 3072
assert "Escape" in js and "aria-expanded" in js
assert not re.search(r'fetch|XMLHttpRequest|localStorage|cookie', js)
assert 4 <= h.count('class="card service-card"') <= 6
assert h.count('class="card doctor-card"') == 3
print("OK")

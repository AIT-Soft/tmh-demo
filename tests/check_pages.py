import re
import pathlib

s = pathlib.Path(__file__).parent.parent / "site"
titles = set()
for name, cur in (("gioi-thieu.html", "gioi-thieu.html"), ("doi-ngu.html", "doi-ngu.html")):
    h = (s / name).read_text(encoding="utf-8")
    assert h.count("<h1") == 1, name
    for k in ['lang="vi"', 'og:title', 'og:description', 'content="noindex"', 'rel="icon"',
              'skip-link', 'không phải phòng khám thật']:
        assert k in h, (name, k)
    assert h.count('aria-current="page"') == 1 and f'href="{cur}" aria-current="page"' in h, name
    t = re.search(r"<title>(.*?)</title>", h).group(1)
    assert t not in titles and t != "Phòng khám Tai Mũi Họng Minh Họa – Website demo"
    titles.add(t)
    assert not re.search(r'(src|href)="https?:', h)
    for ref in re.findall(r'(?:src|href)="([^"#:]+)"', h):
        assert (s / ref).exists() or ref in ("dich-vu.html", "lien-he.html"), (name, ref)
g = (s / "gioi-thieu.html").read_text(encoding="utf-8")
assert g.count('class="feature"') == 4 and g.count('class="facility"') == 3
assert g.count("<tr>") == 4 and "07:30 – 17:00" in g
d = (s / "doi-ngu.html").read_text(encoding="utf-8")
assert d.count('class="card doctor-card"') == 5 and d.count("<dt>Kinh nghiệm</dt>") == 5
print("OK")

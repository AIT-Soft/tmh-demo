import re
import pathlib

s = pathlib.Path(__file__).parent.parent / "site"
for name in ("dich-vu.html", "lien-he.html"):
    h = (s / name).read_text(encoding="utf-8")
    assert h.count("<h1") == 1, name
    for k in ['lang="vi"', 'og:title', 'og:description', 'content="noindex"', 'rel="icon"',
              'skip-link', 'không phải phòng khám thật']:
        assert k in h, (name, k)
    assert f'href="{name}" aria-current="page"' in h and h.count('aria-current="page"') == 1
    assert not re.search(r'(src|href)="https?:', h) and "<iframe" not in h
    for ref in re.findall(r'(?:src|href)="([^"#:]+)"', h):
        assert (s / ref).exists(), (name, ref)
d = (s / "dich-vu.html").read_text(encoding="utf-8")
arts = re.findall(r"<article.*?</article>", d, re.S)
assert len(arts) >= 6
for a in arts:
    p = re.search(r"<p>(.*?)</p>", a, re.S).group(1)
    assert 20 <= len(p.split()) <= 60, p
assert "chỉ mang tính giới thiệu" in d
l = (s / "lien-he.html").read_text(encoding="utf-8")
for k in ["Địa chỉ", 'href="tel:0000000000"', "lienhe@example.com", "Giờ làm việc", "map.svg", "form.js",
          "Vui lòng nhập họ và tên.", "Vui lòng chọn một dịch vụ.", "Vui lòng nhập số điện thoại"]:
    assert k in l, k
assert "<form" in l and "action=" not in l and l.count("aria-describedby") >= 3
assert len(re.findall(r"<label ", l)) == 5
js = s / "assets" / "js"
assert (js / "form.js").stat().st_size <= 4096
for f in js.glob("*.js"):
    assert not re.search(r"fetch|XMLHttpRequest|localStorage|sessionStorage|cookie", f.read_text(), re.I), f
print("OK")

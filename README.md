# tmh-demo

Static demo website for a fictional ENT (Ear, Nose, Throat) clinic: Home, About, Team, Services, Contact.
Website demo giới thiệu phòng khám Tai Mũi Họng (5 trang tĩnh). Toàn bộ tên, địa chỉ, số điện thoại và nội dung đều là **dữ liệu giả, minh họa**, không phải phòng khám thật.

- Live demo: https://tmh-demo.genalpha.dev
- Plain HTML + CSS + a little JavaScript; no backend, no cookies, no tracking, no third-party assets. Illustrations are hand-drawn SVG.

## Run locally

Open `site/index.html` in a browser, or `python -m http.server -d site`.
Static checks: `python tests/check_home.py`, `python tests/check_pages.py`, `python tests/check_contact.py`.

MIT License. By AIT Software.

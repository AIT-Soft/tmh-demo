# CODEMAP – tmh-demo (site tĩnh)

## Cấu trúc
- `site/` – gốc site tĩnh (build_dir sẽ là ops/site)
- `site/assets/css/style.css` – CSS dùng chung (chép từ documents/design)
- `site/assets/img/` – 19 SVG (logo, favicon, icon dịch vụ, avatar, minh họa)
- `site/assets/js/main.js` – thêm class `js`, menu thu gọn (aria-expanded, Esc)
- `tests/` – kiểm tra tĩnh bằng Python

## Tính năng
ID | tính năng | tệp:hàm/lớp chính | route | test | ghi chú
---|---|---|---|---|---
FR-02/FR-12 | Khung site, nav 5 mục, skip link, menu thu gọn | site/index.html, site/assets/js/main.js | /index.html | tests/check_home.py | trang khác chép khung head/header/footer từ index.html
FR-03/FR-10 | Trang chủ 6 khối + dải demo | site/index.html | /index.html | tests/check_home.py | nội dung từ documents/content/trang-chu.md
FR-04/FR-10 | Trang Giới thiệu: câu chuyện, 4 giá trị, 3 cơ sở vật chất, bảng giờ | site/gioi-thieu.html | /gioi-thieu.html | tests/check_pages.py | nội dung từ gioi-thieu.md
FR-05/FR-10 | Trang Đội ngũ: 5 hồ sơ bác sĩ + avatar SVG | site/doi-ngu.html | /doi-ngu.html | tests/check_pages.py | nội dung từ doi-ngu.md
FR-06/FR-10 | Trang Dịch vụ: ghi chú chung + 6 thẻ dịch vụ (id neo) | site/dich-vu.html | /dich-vu.html | tests/check_contact.py | nội dung từ dich-vu.md
FR-07/FR-10 | Trang Liên hệ: 4 mục liên hệ + bản đồ map.svg (img, không iframe) | site/lien-he.html | /lien-he.html | tests/check_contact.py | nội dung từ lien-he.md
FR-08/FR-09 | Form đặt lịch demo: kiểm tra họ tên/SĐT/dịch vụ, lỗi bằng chữ + aria-describedby, chặn gửi, thông báo demo | site/assets/js/form.js, form trong site/lien-he.html | /lien-he.html | tests/check_contact.py | không action, không mạng/lưu trữ; main.js không đổi

## Điểm mở rộng
Trang mới: chép khung từ index.html, đổi title/description/og và `aria-current`.

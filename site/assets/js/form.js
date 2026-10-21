(function () {
  var f = document.querySelector('form.form');
  if (!f) return;
  var ok = f.querySelector('.alert--success');
  function bad(el) {
    var v = el.value.trim();
    if (el.name === 'so-dien-thoai') return !/^[0-9 .+()-]+$/.test(v) || v.replace(/\D/g, '').length < 8;
    return !v;
  }
  f.addEventListener('submit', function (e) {
    e.preventDefault();
    var first = null;
    Array.prototype.forEach.call(f.querySelectorAll('[required]'), function (el) {
      var err = document.getElementById(el.getAttribute('aria-describedby'));
      var b = bad(el);
      err.hidden = !b;
      if (b) {
        el.setAttribute('aria-invalid', 'true');
        first = first || el;
      } else {
        el.removeAttribute('aria-invalid');
      }
    });
    if (first) { first.focus(); return; }
    f.reset();
    ok.hidden = false;
    ok.focus();
  });
})();

(function () {
  var d = document;
  d.documentElement.classList.add('js');
  d.addEventListener('DOMContentLoaded', function () {
    var b = d.querySelector('.nav-toggle');
    if (!b) return;
    function open() { return b.getAttribute('aria-expanded') === 'true'; }
    b.addEventListener('click', function () {
      b.setAttribute('aria-expanded', open() ? 'false' : 'true');
    });
    d.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && open()) {
        b.setAttribute('aria-expanded', 'false');
        b.focus();
      }
    });
  });
})();

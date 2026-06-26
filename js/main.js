/* ============================================================
   Oakmont Services — homepage interactions
   ------------------------------------------------------------
   Standalone vanilla-JS port of the original Claude Design
   runtime: Lucide icons, hover styles, scroll reveals, sticky
   header state and parallax. No framework, no build step.
   ============================================================ */
(function () {
  'use strict';

  var root = document.getElementById('oak-home');
  if (!root) return;

  /* --- Lucide icons (retry until the CDN script is ready) --- */
  function drawIcons() {
    if (window.lucide && window.lucide.createIcons) {
      window.lucide.createIcons({ attrs: { 'stroke-width': 1.4, width: 26, height: 26 } });
    } else {
      setTimeout(drawIcons, 120);
    }
  }
  drawIcons();

  /* --- style-hover: apply an extra declaration block while hovered.
         Replaces the editor's `style-hover` attribute handling.
         The base style is snapshotted at hover time so it composes
         with styles other handlers (header/parallax) may have set. --- */
  root.querySelectorAll('[style-hover]').forEach(function (el) {
    var hover = el.getAttribute('style-hover');
    if (!hover) return;
    var saved = null;
    el.addEventListener('mouseenter', function () {
      saved = el.getAttribute('style') || '';
      el.setAttribute('style', saved + ';' + hover);
    });
    el.addEventListener('mouseleave', function () {
      if (saved !== null) el.setAttribute('style', saved);
    });
  });

  /* --- Scroll reveals (re-queries the live DOM each pass) --- */
  function checkReveals() {
    var vh = window.innerHeight || document.documentElement.clientHeight;
    root.querySelectorAll('[data-reveal]:not(.oak-in)').forEach(function (el) {
      var r = el.getBoundingClientRect();
      if (r.top < vh * 0.9 && r.bottom > -40) el.classList.add('oak-in');
    });
  }

  /* --- Header state + parallax (rAF-throttled) --- */
  var scrolled = null;
  var ticking = false;

  function apply() {
    var y = window.scrollY || document.documentElement.scrollTop || 0;
    var isScrolled = y > 48;
    if (isScrolled !== scrolled) {
      scrolled = isScrolled;
      var header = document.getElementById('oak-header');
      if (header) {
        header.style.background = isScrolled ? 'rgba(250,248,244,0.9)' : 'transparent';
        header.style.backdropFilter = isScrolled ? 'blur(14px)' : 'none';
        header.style.webkitBackdropFilter = isScrolled ? 'blur(14px)' : 'none';
        header.style.boxShadow = isScrolled ? '0 1px 0 var(--border-subtle)' : 'none';
      }
      root.querySelectorAll('[data-headtxt]').forEach(function (el) {
        el.style.color = isScrolled ? 'var(--text-primary)' : 'var(--oak-ivory)';
      });
    }
    root.querySelectorAll('[data-parallax]').forEach(function (p) {
      var s = parseFloat(p.dataset.parallax) || 0.12;
      var rect = p.getBoundingClientRect();
      var off = (rect.top + rect.height / 2) - (window.innerHeight / 2);
      p.style.transform = 'translateY(' + (-off * s).toFixed(1) + 'px)';
    });
    checkReveals();
    ticking = false;
  }

  function onScroll() {
    if (!ticking) { window.requestAnimationFrame(apply); ticking = true; }
  }

  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll, { passive: true });

  // Double rAF so the hidden state paints first and the entrance plays.
  requestAnimationFrame(function () { requestAnimationFrame(apply); });
  setTimeout(checkReveals, 300);
  setTimeout(checkReveals, 1200);
})();

/* ============================================================
   Oakmont Services — scene engine
   ------------------------------------------------------------
   Vanilla JS, no dependencies. One passive scroll listener and
   one rAF loop drive every scroll-linked scene by writing a
   single custom property (--p, 0 → 1) that CSS turns into
   transforms, opacity, filter and clip-path.
   Everything degrades to a static, readable page under
   prefers-reduced-motion or if this file fails to load.
   ============================================================ */
(function () {
  'use strict';

  var doc = document.documentElement;
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var mqDesktop = window.matchMedia('(min-width: 901px)');
  var finePointer = window.matchMedia('(hover: hover) and (pointer: fine)').matches;

  /* ---------- Icons ---------- */
  (function drawIcons(tries) {
    if (window.lucide && window.lucide.createIcons) {
      window.lucide.createIcons();
    } else if (tries < 40) {
      setTimeout(function () { drawIcons(tries + 1); }, 120);
    }
  })(0);

  /* ---------- Manifesto: split words (keeps text accessible) ---------- */
  document.querySelectorAll('[data-words]').forEach(function (el) {
    var text = el.textContent.trim();
    el.setAttribute('aria-label', text);
    var keys = ['estrategia,', 'arquitectura', 'ejecución', 'sistema', 'único.'];
    var words = text.split(/\s+/);
    el.textContent = '';
    words.forEach(function (w, i) {
      var s = document.createElement('span');
      s.className = 'w' + (keys.indexOf(w) > -1 ? ' w--key' : '');
      s.setAttribute('aria-hidden', 'true');
      s.style.setProperty('--i', i);
      s.textContent = w;
      el.appendChild(s);
      if (i < words.length - 1) el.appendChild(document.createTextNode(' '));
    });
    el.style.setProperty('--n', words.length);
  });

  /* ---------- Reveal + stagger ---------- */
  document.querySelectorAll('[data-stagger]').forEach(function (group) {
    Array.prototype.forEach.call(group.children, function (el, i) {
      if (el.classList.contains('rv')) el.style.setProperty('--i', i);
    });
  });

  var revealables = document.querySelectorAll('.rv, .lines');
  if (reduced || !('IntersectionObserver' in window)) {
    revealables.forEach(function (el) { el.classList.add('is-in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.classList.add('is-in');
        io.unobserve(e.target);
      });
    }, { threshold: 0.18, rootMargin: '0px 0px -6% 0px' });
    revealables.forEach(function (el) { io.observe(el); });
    // Hero plays on load, not on intersection.
    requestAnimationFrame(function () {
      requestAnimationFrame(function () {
        document.querySelectorAll('.hero .rv, .hero .lines').forEach(function (el) { el.classList.add('is-in'); });
      });
    });
  }

  /* ---------- Sticky story (framework) ---------- */
  document.querySelectorAll('[data-sticky-story]').forEach(function (story) {
    var steps = story.querySelectorAll('[data-step]');
    var rings = story.querySelectorAll('.orbit__ring');
    var labels = story.querySelectorAll('.orbit__labels text');
    function activate(idx) {
      steps.forEach(function (s) { s.classList.toggle('is-active', +s.dataset.step === idx); });
      rings.forEach(function (r) {
        var n = +r.dataset.ring;
        r.classList.toggle('is-lit', n <= idx);
        r.classList.toggle('is-on', n === idx);
      });
      labels.forEach(function (t) { t.classList.toggle('is-on', +t.dataset.ring <= idx); });
    }
    activate(0);
    if (!('IntersectionObserver' in window)) return;
    var so = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) activate(+e.target.dataset.step); });
    }, { rootMargin: '-45% 0px -45% 0px' });
    steps.forEach(function (s) { so.observe(s); });
  });

  /* ---------- Mobile menu ---------- */
  var toggle = document.querySelector('.nav__toggle');
  var menu = document.getElementById('menu');
  function setMenu(open) {
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
    menu.hidden = !open;
    document.body.style.overflow = open ? 'hidden' : '';
  }
  if (toggle && menu) {
    toggle.addEventListener('click', function () { setMenu(toggle.getAttribute('aria-expanded') !== 'true'); });
    menu.addEventListener('click', function (e) { if (e.target.closest('a')) setMenu(false); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !menu.hidden) { setMenu(false); toggle.focus(); } });
  }

  /* ---------- Active nav link ---------- */
  var navLinks = document.querySelectorAll('[data-nav-link]');
  if ('IntersectionObserver' in window) {
    var targets = [];
    navLinks.forEach(function (a) { var t = document.querySelector(a.getAttribute('href')); if (t) targets.push(t); });
    var no = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        navLinks.forEach(function (a) {
          var on = a.getAttribute('href') === '#' + e.target.id;
          a.classList.toggle('is-active', on);
          if (on) a.setAttribute('aria-current', 'true'); else a.removeAttribute('aria-current');
        });
      });
    }, { rootMargin: '-40% 0px -55% 0px' });
    targets.forEach(function (t) { no.observe(t); });
  }

  /* ---------- Bento cursor light ---------- */
  if (finePointer && !reduced) {
    document.querySelectorAll('.tile').forEach(function (tile) {
      tile.addEventListener('pointermove', function (e) {
        var r = tile.getBoundingClientRect();
        tile.style.setProperty('--mx', (e.clientX - r.left) + 'px');
        tile.style.setProperty('--my', (e.clientY - r.top) + 'px');
      });
    });

    /* Magnetic CTA */
    document.querySelectorAll('.magnetic').forEach(function (btn) {
      btn.addEventListener('pointermove', function (e) {
        var r = btn.getBoundingClientRect();
        var x = (e.clientX - r.left - r.width / 2) * 0.22;
        var y = (e.clientY - r.top - r.height / 2) * 0.3;
        btn.style.transform = 'translate3d(' + x.toFixed(1) + 'px,' + y.toFixed(1) + 'px,0)';
      });
      btn.addEventListener('pointerleave', function () { btn.style.transform = ''; });
    });
  }

  /* ---------- Hero field: architectural dot grid lit by the pointer ---------- */
  var canvas = document.querySelector('.hero__field');
  var field = null;
  if (canvas && canvas.getContext) {
    var ctx = canvas.getContext('2d');
    var W = 0, H = 0, dpr = 1, gap = 34, t0 = performance.now();
    var mouse = { x: -9999, y: -9999, tx: -9999, ty: -9999 };
    var running = false;

    function size() {
      dpr = Math.min(window.devicePixelRatio || 1, 2);
      W = canvas.clientWidth; H = canvas.clientHeight;
      canvas.width = W * dpr; canvas.height = H * dpr;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      gap = W < 700 ? 28 : 34;
    }
    function draw(now) {
      var t = (now - t0) / 1000;
      ctx.clearRect(0, 0, W, H);
      mouse.x += (mouse.tx - mouse.x) * 0.08;
      mouse.y += (mouse.ty - mouse.y) * 0.08;
      for (var y = gap / 2; y < H; y += gap) {
        for (var x = gap / 2; x < W; x += gap) {
          // slow travelling swell, like light moving across stone
          var wave = Math.sin(x * 0.006 + t * 0.5) * Math.cos(y * 0.008 - t * 0.35);
          var dx = x - mouse.x, dy = y - mouse.y;
          var d = Math.sqrt(dx * dx + dy * dy);
          var lit = Math.max(0, 1 - d / 260);
          var a = 0.07 + (wave + 1) * 0.045 + lit * 0.55;
          var r = 0.8 + lit * 1.3;
          ctx.fillStyle = lit > 0.02 ? 'rgba(196,181,150,' + a.toFixed(3) + ')' : 'rgba(247,247,247,' + a.toFixed(3) + ')';
          ctx.beginPath();
          ctx.arc(x, y + wave * 2, r, 0, 6.2832);
          ctx.fill();
        }
      }
      if (running) requestAnimationFrame(draw);
    }
    function start() { if (!running && !reduced) { running = true; requestAnimationFrame(draw); } }
    function stop() { running = false; }

    size();
    if (reduced) { draw(performance.now()); }
    window.addEventListener('resize', function () { size(); if (!running) draw(performance.now()); }, { passive: true });
    if (finePointer) {
      window.addEventListener('pointermove', function (e) {
        var r = canvas.getBoundingClientRect();
        mouse.tx = e.clientX - r.left; mouse.ty = e.clientY - r.top;
      }, { passive: true });
    }
    field = { start: start, stop: stop };
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (en) { en[0].isIntersecting ? start() : stop(); }).observe(canvas);
    } else { start(); }
  }

  /* ---------- Scroll engine ---------- */
  var nav = document.getElementById('nav');
  var bar = document.querySelector('.progress span');
  var scrubs = Array.prototype.slice.call(document.querySelectorAll('[data-scrub]'));
  var hscroll = document.querySelector('[data-hscroll]');
  var hTrack = hscroll && hscroll.querySelector('.journey__track');
  var parallax = Array.prototype.slice.call(document.querySelectorAll('[data-parallax]'));
  var hero = document.querySelector('.hero');
  var lastY = window.scrollY, ticking = false, hDistance = 0;

  function layoutHScroll() {
    if (!hscroll || !hTrack) return;
    if (reduced || !mqDesktop.matches) {
      hscroll.style.height = '';
      hTrack.style.removeProperty('--x');
      hDistance = 0;
      return;
    }
    hDistance = Math.max(0, hTrack.scrollWidth - window.innerWidth);
    hscroll.style.height = (window.innerHeight + hDistance) + 'px';
  }

  function progressOf(el) {
    var r = el.getBoundingClientRect();
    var span = r.height - window.innerHeight;
    if (span <= 0) return r.top <= 0 ? 1 : 0;
    return Math.min(1, Math.max(0, -r.top / span));
  }

  function frame() {
    ticking = false;
    var y = window.scrollY;
    var vh = window.innerHeight;

    // progress bar
    var max = doc.scrollHeight - vh;
    if (bar) bar.style.transform = 'scaleX(' + (max > 0 ? Math.min(1, y / max) : 0).toFixed(4) + ')';

    // nav: transparent on the hero, glass afterwards, hides while reading downward
    if (nav) {
      var heroEnd = hero ? hero.offsetHeight - vh * 0.6 : vh;
      nav.classList.toggle('is-solid', y > Math.min(heroEnd, vh * 0.9));
      var menuOpen = menu && !menu.hidden;
      nav.classList.toggle('is-hidden', !menuOpen && y > vh && y > lastY + 2);
      if (y < lastY - 2) nav.classList.remove('is-hidden');
    }
    lastY = y;

    if (reduced) return;

    scrubs.forEach(function (el) {
      var r = el.getBoundingClientRect();
      if (r.bottom < -vh || r.top > vh * 1.5) return;
      el.style.setProperty('--p', progressOf(el).toFixed(4));
    });

    if (hscroll && hDistance > 0) {
      var p = progressOf(hscroll);
      hscroll.style.setProperty('--p', p.toFixed(4));
      hTrack.style.setProperty('--x', (p * hDistance).toFixed(1));
    }

    if (mqDesktop.matches) {
      parallax.forEach(function (el) {
        var r = el.getBoundingClientRect();
        if (r.bottom < -200 || r.top > vh + 200) return;
        var speed = parseFloat(el.dataset.parallax) || 0.06;
        var off = (r.top + r.height / 2 - vh / 2) * -speed;
        el.style.transform = 'translate3d(0,' + off.toFixed(1) + 'px,0)';
      });
    }
  }

  function request() { if (!ticking) { ticking = true; requestAnimationFrame(frame); } }

  layoutHScroll();
  frame();
  window.addEventListener('scroll', request, { passive: true });
  window.addEventListener('resize', function () { layoutHScroll(); request(); }, { passive: true });
  window.addEventListener('load', function () { layoutHScroll(); request(); });
  if (mqDesktop.addEventListener) mqDesktop.addEventListener('change', function () { layoutHScroll(); parallax.forEach(function (el) { el.style.transform = ''; }); request(); });
})();

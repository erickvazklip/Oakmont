/* ============================================================
   Oakmont Services — interactions
   ------------------------------------------------------------
   Small on purpose: icons, one-time reveals, header state,
   active section in the nav and the mobile menu.
   No scroll-linked animation and no continuous rAF loops.
   The page is fully readable if this file never runs.
   ============================================================ */
(function () {
  'use strict';

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var hasIO = 'IntersectionObserver' in window;

  /* ---------- Icons ---------- */
  (function drawIcons(tries) {
    if (window.lucide && window.lucide.createIcons) window.lucide.createIcons();
    else if (tries < 40) setTimeout(function () { drawIcons(tries + 1); }, 120);
  })(0);

  /* ---------- One-time reveals ---------- */
  document.querySelectorAll('[data-stagger]').forEach(function (group) {
    Array.prototype.forEach.call(group.children, function (el, i) { el.style.setProperty('--i', i); });
  });

  var items = document.querySelectorAll('.rv, .lines');
  if (reduced || !hasIO) {
    items.forEach(function (el) { el.classList.add('is-in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.classList.add('is-in');
        io.unobserve(e.target);
      });
    }, { threshold: 0.15, rootMargin: '0px 0px -5% 0px' });
    items.forEach(function (el) { io.observe(el); });
  }

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
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && !menu.hidden) { setMenu(false); toggle.focus(); }
    });
  }

  /* ---------- Header: solid once the hero is left behind ---------- */
  var nav = document.getElementById('nav');
  var hero = document.querySelector('.hero');
  if (nav && hero && hasIO) {
    new IntersectionObserver(function (entries) {
      nav.classList.toggle('is-solid', !entries[0].isIntersecting);
    }, { rootMargin: '-80px 0px 0px 0px' }).observe(hero);
  } else if (nav) {
    nav.classList.add('is-solid');
  }

  /* ---------- Dropdowns: hover/focus via CSS; click + Escape for touch and keyboard ---------- */
  var menuItems = document.querySelectorAll('.nav__item.has-menu');
  function closeAll(except) {
    menuItems.forEach(function (it) {
      if (it === except) return;
      it.classList.remove('is-open');
      var b = it.querySelector('.nav__caret');
      if (b) b.setAttribute('aria-expanded', 'false');
    });
  }
  menuItems.forEach(function (item) {
    var btn = item.querySelector('.nav__caret');
    if (!btn) return;
    btn.addEventListener('click', function (ev) {
      ev.stopPropagation();
      var open = !item.classList.contains('is-open');
      closeAll(item);
      item.classList.toggle('is-open', open);
      btn.setAttribute('aria-expanded', String(open));
    });
    item.addEventListener('mouseleave', function () {
      item.classList.remove('is-open');
      btn.setAttribute('aria-expanded', 'false');
    });
  });
  document.addEventListener('click', function (ev) { if (!ev.target.closest('.nav__item')) closeAll(); });
  document.addEventListener('keydown', function (ev) {
    if (ev.key !== 'Escape') return;
    var open = document.querySelector('.nav__item.is-open');
    if (!open) return;
    closeAll();
    open.querySelector('.nav__caret').focus();
  });
  menuItems.forEach(function (item) {
    item.addEventListener('focusout', function (ev) {
      if (!item.contains(ev.relatedTarget)) {
        item.classList.remove('is-open');
        var b = item.querySelector('.nav__caret');
        if (b) b.setAttribute('aria-expanded', 'false');
      }
    });
  });

  /* ---------- Contact form: validate, then compose an email ---------- */
  var form = document.getElementById('contact-form');
  if (form) {
    var params = new URLSearchParams(window.location.search);
    var pre = params.get('interes');
    if (pre && form.interes.querySelector('option[value="' + pre.replace(/[^a-z0-9-]/g, '') + '"]')) {
      form.interes.value = pre;
    }
    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      var ok = true;
      form.querySelectorAll('[required]').forEach(function (el) {
        var valid = el.type === 'checkbox' ? el.checked : el.value.trim() !== '' && (el.type !== 'email' || /.+@.+\..+/.test(el.value));
        var wrap = el.closest('.field, .check');
        if (wrap) wrap.classList.toggle('is-invalid', !valid);
        if (!valid && ok) { el.focus(); ok = false; }
      });
      form.querySelector('.form__error').hidden = ok;
      if (!ok) return;
      var topic = form.interes.options[form.interes.selectedIndex].text;
      var lines = [
        'Nombre: ' + form.nombre.value,
        'Correo: ' + form.correo.value,
        'Empresa: ' + form.empresa.value,
        'Cargo: ' + form.cargo.value,
        'Teléfono: ' + form.telefono.value,
        'Tema: ' + topic,
        '',
        form.mensaje.value
      ];
      var to = form.getAttribute('action').replace('mailto:', '');
      var subject = 'Contacto web — ' + topic + ' — ' + form.empresa.value;
      window.location.href = 'mailto:' + to + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(lines.join('\n'));
      form.querySelector('.form__ok').hidden = false;
    });
  }

  /* ---------- Active section in the nav ---------- */
  var links = document.querySelectorAll('[data-nav-link]');
  if (hasIO && links.length) {
    var so = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        links.forEach(function (a) {
          var on = a.getAttribute('href') === '#' + e.target.id;
          a.classList.toggle('is-active', on);
          if (on) a.setAttribute('aria-current', 'true'); else a.removeAttribute('aria-current');
        });
      });
    }, { rootMargin: '-40% 0px -55% 0px' });
    links.forEach(function (a) {
      var t = document.querySelector(a.getAttribute('href'));
      if (t) so.observe(t);
    });
  }
})();

/* ============================================================
   Oakmont Services — interactions
   ------------------------------------------------------------
   Small on purpose: one-time reveals, header state, dropdowns,
   mobile menu, contact form and the cursor. No scroll-linked animation.
   Every page is fully readable if this file never runs.
   ============================================================ */
(function () {
  'use strict';

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var hasIO = 'IntersectionObserver' in window;

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

  /* ---------- Header: transparent over the home hero, solid elsewhere ---------- */
  var nav = document.getElementById('nav');
  var hero = document.querySelector('.hero');
  if (nav && hero && hasIO) {
    new IntersectionObserver(function (entries) {
      nav.classList.toggle('is-solid', !entries[0].isIntersecting);
    }, { rootMargin: '-80px 0px 0px 0px' }).observe(hero);
  } else if (nav) {
    nav.classList.add('is-solid');
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
  }

  /* ---------- Dropdowns: hover via CSS; button for touch and keyboard ---------- */
  var dropdowns = document.querySelectorAll('.nav__item.has-menu');
  function setOpen(item, open) {
    item.classList.toggle('is-open', open);
    item.querySelector('.nav__caret').setAttribute('aria-expanded', String(open));
  }
  dropdowns.forEach(function (item) {
    item.querySelector('.nav__caret').addEventListener('click', function (ev) {
      ev.stopPropagation();
      var open = !item.classList.contains('is-open');
      dropdowns.forEach(function (other) { if (other !== item) setOpen(other, false); });
      setOpen(item, open);
    });
    item.addEventListener('mouseleave', function () { setOpen(item, false); });
    item.addEventListener('focusout', function (ev) { if (!item.contains(ev.relatedTarget)) setOpen(item, false); });
  });
  document.addEventListener('click', function (ev) {
    if (!ev.target.closest('.nav__item')) dropdowns.forEach(function (it) { setOpen(it, false); });
  });

  /* ---------- Escape closes whatever is open ---------- */
  document.addEventListener('keydown', function (ev) {
    if (ev.key !== 'Escape') return;
    if (menu && !menu.hidden) { setMenu(false); toggle.focus(); return; }
    var open = document.querySelector('.nav__item.is-open');
    if (open) { setOpen(open, false); open.querySelector('.nav__caret').focus(); }
  });

  /* ---------- Contact form: validate, then POST to /api/contacto ---------- */
  var form = document.getElementById('contact-form');
  if (form) {
    var params = new URLSearchParams(window.location.search);
    var okBox = form.querySelector('.form__ok');
    var errBox = form.querySelector('.form__error');
    var fallback = ' Si el problema continúa, escríbanos a ' + form.getAttribute('data-email') + '.';

    var pre = (params.get('interes') || '').replace(/[^a-z0-9-]/g, '');
    if (pre && form.interes.querySelector('option[value="' + pre + '"]')) form.interes.value = pre;
    if (params.get('enviado')) form.classList.add('is-sent');
    if (params.get('error')) { errBox.textContent = 'No pudimos registrar su mensaje.' + fallback; errBox.hidden = false; }
    form.ts.value = String(Date.now());
    form.pagina_origen.value = document.referrer || window.location.href;

    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      var ok = true;
      form.querySelectorAll('[required]').forEach(function (el) {
        var v = el.value.trim();
        var valid = el.type === 'checkbox' ? el.checked : v !== '' && (el.type !== 'email' || /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v));
        el.closest('.field, .check').classList.toggle('is-invalid', !valid);
        if (!valid && ok) { el.focus(); ok = false; }
      });
      errBox.textContent = 'Revise los campos marcados con *.';
      errBox.hidden = ok;
      if (!ok) return;

      form.interes_label.value = form.interes.options[form.interes.selectedIndex].text;
      var data = {};
      new FormData(form).forEach(function (v, k) { data[k] = v; });
      data.privacidad = form.privacidad.checked;

      var btn = form.querySelector('button[type=submit]');
      var label = btn.textContent;
      btn.disabled = true; btn.textContent = 'Enviando…';
      fetch(form.getAttribute('action'), {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
      }).then(function (r) {
        return r.json().catch(function () { return {}; }).then(function (j) {
          if (!r.ok || !j.ok) throw new Error(j.error || '');
        });
      }).then(function () {
        form.reset();
        form.classList.add('is-sent');
        okBox.focus();
      }).catch(function (err) {
        errBox.textContent = (err.message || 'No pudimos enviar su mensaje.') + fallback;
        errBox.hidden = false;
      }).then(function () {
        btn.disabled = false; btn.textContent = label;
      });
    });
  }
  /* ---------- Cursor: gold dot + trailing ring, echoing the diagrams' orbits ---------- */
  if (window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
    var cur = document.createElement('div');
    cur.className = 'cursor';
    cur.setAttribute('aria-hidden', 'true');
    cur.innerHTML = '<span class="cursor__ring"></span><span class="cursor__dot"></span>';
    document.body.appendChild(cur);
    document.documentElement.classList.add('has-cursor');
    var ring = cur.firstChild, dotEl = cur.lastChild;
    var x = -100, y = -100, rx = x, ry = y, raf = null, follow = reduced ? 1 : 0.2;
    var place = function (el, px, py) { el.style.transform = 'translate3d(' + px + 'px,' + py + 'px,0)'; };
    var trail = function () {
      rx += (x - rx) * follow; ry += (y - ry) * follow;
      place(ring, rx.toFixed(1), ry.toFixed(1));
      raf = Math.abs(x - rx) + Math.abs(y - ry) > 0.2 ? requestAnimationFrame(trail) : null;
    };
    var interactive = 'a, button, summary, select, label, [role="button"]';
    var textual = 'input:not([type="checkbox"]):not([type="radio"]), textarea';
    document.addEventListener('pointermove', function (e) {
      x = e.clientX; y = e.clientY;
      place(dotEl, x, y);
      cur.classList.add('is-visible');
      if (!raf) raf = requestAnimationFrame(trail);
    }, { passive: true });
    document.addEventListener('pointerover', function (e) {
      cur.classList.toggle('is-link', !!e.target.closest(interactive));
      cur.classList.toggle('is-text', !!e.target.closest(textual));
    });
    document.addEventListener('pointerdown', function () { cur.classList.add('is-down'); });
    document.addEventListener('pointerup', function () { cur.classList.remove('is-down'); });
    document.documentElement.addEventListener('pointerleave', function () { cur.classList.remove('is-visible'); });
  }
})();

/* ============================================================
   Oakmont Services — interactions
   ------------------------------------------------------------
   Small on purpose: one-time reveals, header state, dropdowns
   and the mobile menu. No scroll-linked animation.
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
})();

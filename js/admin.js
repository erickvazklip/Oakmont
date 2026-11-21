/* Oakmont — leads admin panel. Talks to /api/leads with the admin password
   as a Bearer token. The password is kept only in sessionStorage. */
(function () {
  'use strict';
  var KEY = 'oak_admin_pw';
  var login = document.getElementById('login');
  var panel = document.getElementById('panel');
  var rowsEl = document.getElementById('rows');
  var q = document.getElementById('q');
  var all = [];

  function pw() { try { return sessionStorage.getItem(KEY) || ''; } catch (e) { return ''; } }
  function setPw(v) { try { v ? sessionStorage.setItem(KEY, v) : sessionStorage.removeItem(KEY); } catch (e) {} }
  function api(path, opts) {
    opts = opts || {};
    opts.headers = Object.assign({ Authorization: 'Bearer ' + pw() }, opts.headers || {});
    return fetch('/api/leads' + (path || ''), opts);
  }
  function text(s) { var d = document.createElement('div'); d.textContent = s == null ? '' : String(s); return d.innerHTML; }
  function fmt(iso) {
    try { return new Date(iso).toLocaleString('es-MX', { dateStyle: 'medium', timeStyle: 'short' }); } catch (e) { return iso; }
  }

  function showLogin(msg) {
    panel.hidden = true; login.hidden = false;
    var err = document.getElementById('login-err');
    err.hidden = !msg; err.textContent = msg || '';
    login.pw.focus();
  }

  function render() {
    var term = q.value.trim().toLowerCase();
    var list = all.filter(function (l) {
      if (!term) return true;
      return [l.nombre, l.empresa, l.correo, l.interes_label, l.cargo, l.mensaje].join(' ').toLowerCase().indexOf(term) > -1;
    });
    document.getElementById('count').textContent = list.length + ' de ' + all.length + ' leads';
    document.getElementById('empty').hidden = all.length > 0;
    rowsEl.innerHTML = list.map(function (l, i) {
      return '<tr class="lead" data-i="' + i + '" tabindex="0" aria-expanded="false">' +
        '<td>' + text(fmt(l.fecha)) + '</td><td>' + text(l.nombre) + '</td><td>' + text(l.empresa) + '</td><td>' + text(l.cargo) + '</td>' +
        '<td><a href="mailto:' + text(l.correo) + '">' + text(l.correo) + '</a></td><td>' + text(l.telefono) + '</td><td>' + text(l.interes_label || l.interes) + '</td>' +
        '<td><button class="adm-del" data-path="' + text(l.path) + '" type="button">Eliminar</button></td></tr>' +
        '<tr class="msg" hidden><td colspan="8">' + text(l.mensaje) + (l.pagina_origen ? '\n\nOrigen: ' + text(l.pagina_origen) : '') + '</td></tr>';
    }).join('');
  }

  function load() {
    document.getElementById('panel-err').hidden = true;
    return api('').then(function (r) {
      if (r.status === 401) { setPw(''); showLogin('Contraseña incorrecta.'); return; }
      return r.json().then(function (j) {
        if (!j.ok) throw new Error(j.error || 'Error');
        all = j.leads || [];
        login.hidden = true; panel.hidden = false;
        render();
      });
    }).catch(function (e) {
      var el = document.getElementById('panel-err');
      el.textContent = 'No se pudo cargar: ' + e.message; el.hidden = false;
    });
  }

  login.addEventListener('submit', function (ev) {
    ev.preventDefault();
    setPw(login.pw.value);
    login.pw.value = '';
    load();
  });

  q.addEventListener('input', render);
  document.getElementById('reload').addEventListener('click', load);
  document.getElementById('logout').addEventListener('click', function () { setPw(''); all = []; rowsEl.innerHTML = ''; showLogin(); });

  document.getElementById('csv').addEventListener('click', function () {
    api('?format=csv').then(function (r) {
      if (!r.ok) throw new Error('Error ' + r.status);
      return r.blob();
    }).then(function (b) {
      var a = document.createElement('a');
      a.href = URL.createObjectURL(b);
      a.download = 'oakmont-leads-' + new Date().toISOString().slice(0, 10) + '.csv';
      document.body.appendChild(a); a.click(); a.remove();
      setTimeout(function () { URL.revokeObjectURL(a.href); }, 1000);
    }).catch(function (e) { alert('No se pudo exportar: ' + e.message); });
  });

  rowsEl.addEventListener('click', function (ev) {
    var del = ev.target.closest('.adm-del');
    if (del) {
      ev.stopPropagation();
      if (!confirm('¿Eliminar este lead de forma permanente?')) return;
      api('?path=' + encodeURIComponent(del.getAttribute('data-path')), { method: 'DELETE' })
        .then(function (r) { if (!r.ok) throw new Error('Error ' + r.status); return load(); })
        .catch(function (e) { alert('No se pudo eliminar: ' + e.message); });
      return;
    }
    var tr = ev.target.closest('tr.lead');
    if (!tr || ev.target.closest('a')) return;
    var msg = tr.nextElementSibling;
    msg.hidden = !msg.hidden;
    tr.setAttribute('aria-expanded', String(!msg.hidden));
  });
  rowsEl.addEventListener('keydown', function (ev) {
    if ((ev.key === 'Enter' || ev.key === ' ') && ev.target.matches('tr.lead')) { ev.preventDefault(); ev.target.click(); }
  });

  if (pw()) load(); else showLogin();
})();

import { test, mock } from 'node:test';
import assert from 'node:assert/strict';

const store = new Map();
mock.module('@vercel/blob', { namedExports: {
  put: async (p, body, o) => { assert.equal(o.access, 'private'); store.set(p, body); return { pathname: p }; },
  list: async ({ prefix }) => ({ blobs: [...store.keys()].filter(k => k.startsWith(prefix)).map(pathname => ({ pathname })), hasMore: false }),
  get: async (p) => store.has(p) ? { stream: new Response(store.get(p)).body } : null,
  del: async (p) => { store.delete(p); },
}});
process.env.ADMIN_PASSWORD = 'secreto-de-prueba';
const contacto = (await import('../api/contacto.js')).default;
const leads = (await import('../api/leads.js')).default;

function call(h, { method = 'POST', body = {}, headers = {}, query = {} } = {}) {
  return new Promise(resolve => {
    const res = { code: 200, hdr: {}, setHeader(k, v) { this.hdr[k.toLowerCase()] = v; },
      status(c) { this.code = c; return this; },
      json(o) { resolve({ code: this.code, body: o, hdr: this.hdr }); },
      send(s) { resolve({ code: this.code, body: s, hdr: this.hdr }); },
      redirect(c, u) { resolve({ code: c, location: u }); } };
    h({ method, body, query, headers: { 'content-type': 'application/json', ...headers } }, res);
  });
}
const good = { nombre: 'Ana Pérez', correo: 'ana@empresa.com', empresa: 'Empresa, S.A.', cargo: 'CIO', telefono: '+52 55', interes: 'data-ai', interes_label: 'Data & AI', mensaje: '=HYPERLINK("x") prueba', privacidad: true, ts: Date.now() - 10000 };

test('lead válido se guarda en privado', async () => {
  const r = await call(contacto, { body: good });
  assert.equal(r.code, 201); assert.ok(r.body.id); assert.equal(store.size, 1);
});
test('faltan campos / sin consentimiento -> 400', async () => {
  assert.equal((await call(contacto, { body: { ...good, empresa: '' } })).code, 400);
  assert.equal((await call(contacto, { body: { ...good, privacidad: false } })).code, 400);
  assert.equal((await call(contacto, { body: { ...good, correo: 'no-es-correo' } })).code, 400);
  assert.equal(store.size, 1);
});
test('spam (honeypot o envío instantáneo) se descarta sin guardar', async () => {
  assert.equal((await call(contacto, { body: { ...good, sitio_web: 'http://spam' } })).code, 200);
  assert.equal((await call(contacto, { body: { ...good, ts: Date.now() } })).code, 200);
  assert.equal(store.size, 1);
});
test('envío sin JS (form-urlencoded) redirige', async () => {
  const r = await call(contacto, { body: { ...good, privacidad: 'on' }, headers: { 'content-type': 'application/x-www-form-urlencoded' } });
  assert.equal(r.code, 303); assert.equal(r.location, '/contacto/?enviado=1'); assert.equal(store.size, 2);
});
test('GET no permitido en contacto', async () => { assert.equal((await call(contacto, { method: 'GET' })).code, 405); });
test('leads requiere contraseña', async () => {
  assert.equal((await call(leads, { method: 'GET' })).code, 401);
  assert.equal((await call(leads, { method: 'GET', headers: { authorization: 'Bearer mala' } })).code, 401);
});
test('leads JSON, CSV y borrado', async () => {
  const auth = { authorization: 'Bearer secreto-de-prueba' };
  const j = await call(leads, { method: 'GET', headers: auth });
  assert.equal(j.code, 200); assert.equal(j.body.total, 2); assert.equal(j.body.leads[0].empresa, 'Empresa, S.A.');
  const c = await call(leads, { method: 'GET', headers: auth, query: { format: 'csv' } });
  assert.match(c.hdr['content-type'], /text\/csv/); assert.ok(c.body.startsWith('﻿"Fecha"'));
  assert.ok(c.body.includes(`"'=HYPERLINK(""x"") prueba"`), 'fórmula neutralizada');
  assert.equal((await call(leads, { method: 'DELETE', headers: auth, query: { path: '../x' } })).code, 400);
  const d = await call(leads, { method: 'DELETE', headers: auth, query: { path: j.body.leads[0].path } });
  assert.equal(d.code, 200); assert.equal(store.size, 1);
});

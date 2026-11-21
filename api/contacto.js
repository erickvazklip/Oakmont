// POST /api/contacto — receives the contact form and stores each lead as a
// private JSON object in Vercel Blob (store connected to this project).
import { put } from '@vercel/blob';
import { randomUUID } from 'node:crypto';
import { PREFIX } from './_lib.js';

const LIMITS = { nombre: 120, correo: 160, empresa: 160, cargo: 120, telefono: 40, interes: 60, interes_label: 120, mensaje: 5000, pagina_origen: 300 };
const REQUIRED = ['nombre', 'correo', 'empresa', 'interes', 'mensaje'];
const EMAIL = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

function clean(v, max) {
  return String(v == null ? '' : v).replace(/[\u0000-\u0008\u000B\u000C\u000E-\u001F]/g, '').trim().slice(0, max);
}

export default async function handler(req, res) {
  const wantsHtml = !(req.headers['content-type'] || '').includes('application/json');

  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    return res.status(405).json({ ok: false, error: 'Método no permitido.' });
  }

  const body = typeof req.body === 'object' && req.body ? req.body : {};

  // Spam guards: hidden honeypot field must stay empty and the form must
  // have been on screen for at least 3 seconds. Bots get a fake success.
  const started = Number(body.ts || 0);
  if (clean(body.sitio_web, 200) !== '' || (started && Date.now() - started < 3000)) {
    return wantsHtml ? res.redirect(303, '/contacto/?enviado=1') : res.status(200).json({ ok: true });
  }

  const lead = {};
  for (const [k, max] of Object.entries(LIMITS)) lead[k] = clean(body[k], max);
  const consent = body.privacidad === true || body.privacidad === 'on' || body.privacidad === 'true';

  const missing = REQUIRED.filter((k) => !lead[k]);
  if (missing.length || !EMAIL.test(lead.correo) || !consent) {
    const error = !consent ? 'Debe aceptar el aviso de privacidad.' : 'Revise los campos obligatorios.';
    return wantsHtml ? res.redirect(303, '/contacto/?error=1') : res.status(400).json({ ok: false, error, missing });
  }

  const now = new Date();
  lead.id = randomUUID();
  lead.fecha = now.toISOString();
  lead.consentimiento_privacidad = true;

  const path = `${PREFIX}${now.toISOString().slice(0, 7)}/${now.getTime()}-${lead.id}.json`;
  try {
    await put(path, JSON.stringify(lead, null, 2), {
      access: 'private',
      contentType: 'application/json',
      addRandomSuffix: false,
    });
  } catch (err) {
    console.error('blob put failed', err);
    return wantsHtml ? res.redirect(303, '/contacto/?error=2') : res.status(500).json({ ok: false, error: 'No pudimos registrar su mensaje. Intente de nuevo o escriba a contacto@oakmontservices.com.' });
  }

  return wantsHtml ? res.redirect(303, '/contacto/?enviado=1') : res.status(201).json({ ok: true, id: lead.id });
}

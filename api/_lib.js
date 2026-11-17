// Shared helpers for the API functions. Files starting with "_" are not
// exposed as endpoints by Vercel.
import { timingSafeEqual } from 'node:crypto';

export const PREFIX = 'leads/';

export const FIELDS = [
  ['fecha', 'Fecha'],
  ['nombre', 'Nombre'],
  ['correo', 'Correo'],
  ['empresa', 'Empresa'],
  ['cargo', 'Cargo'],
  ['telefono', 'Teléfono'],
  ['interes', 'Interés (clave)'],
  ['interes_label', 'Interés'],
  ['mensaje', 'Mensaje'],
  ['pagina_origen', 'Página de origen'],
  ['id', 'ID'],
];

/** Constant-time password check against ADMIN_PASSWORD. */
export function isAuthorized(req) {
  const expected = process.env.ADMIN_PASSWORD || '';
  const header = req.headers.authorization || '';
  const given = header.startsWith('Bearer ') ? header.slice(7) : '';
  if (!expected || !given) return false;
  const a = Buffer.from(given);
  const b = Buffer.from(expected);
  return a.length === b.length && timingSafeEqual(a, b);
}

/** CSV with BOM so Excel opens accents correctly. */
export function toCSV(rows) {
  const esc = (v) => {
    const s = v == null ? '' : String(v);
    // Neutralise spreadsheet formula injection.
    const safe = /^[=+\-@\t\r]/.test(s) ? "'" + s : s;
    return '"' + safe.replace(/"/g, '""') + '"';
  };
  const head = FIELDS.map(([, label]) => esc(label)).join(',');
  const body = rows.map((r) => FIELDS.map(([k]) => esc(r[k])).join(',')).join('\r\n');
  return '﻿' + head + '\r\n' + body + '\r\n';
}

// /api/leads — admin access to stored leads. Requires
//   Authorization: Bearer <ADMIN_PASSWORD>
// GET                 -> JSON list, newest first
// GET ?format=csv     -> CSV download (Excel-friendly)
// DELETE ?path=...    -> deletes one lead (e.g. to honour an ARCO request)
import { list, get, del } from '@vercel/blob';
import { PREFIX, isAuthorized, toCSV } from './_lib.js';

async function readAll() {
  const blobs = [];
  let cursor;
  do {
    const page = await list({ prefix: PREFIX, cursor, limit: 1000 });
    blobs.push(...page.blobs);
    cursor = page.hasMore ? page.cursor : undefined;
  } while (cursor);

  const rows = [];
  const BATCH = 20;
  for (let i = 0; i < blobs.length; i += BATCH) {
    const chunk = await Promise.all(blobs.slice(i, i + BATCH).map(async (b) => {
      const r = await get(b.pathname, { access: 'private', useCache: false });
      if (!r) return null;
      const text = await new Response(r.stream).text();
      try { return { ...JSON.parse(text), path: b.pathname }; } catch { return null; }
    }));
    rows.push(...chunk.filter(Boolean));
  }
  rows.sort((a, b) => String(b.fecha).localeCompare(String(a.fecha)));
  return rows;
}

export default async function handler(req, res) {
  res.setHeader('Cache-Control', 'no-store');
  res.setHeader('X-Robots-Tag', 'noindex');
  if (!isAuthorized(req)) return res.status(401).json({ ok: false, error: 'No autorizado.' });

  try {
    if (req.method === 'GET') {
      const rows = await readAll();
      if (req.query.format === 'csv') {
        const stamp = new Date().toISOString().slice(0, 10);
        res.setHeader('Content-Type', 'text/csv; charset=utf-8');
        res.setHeader('Content-Disposition', `attachment; filename="oakmont-leads-${stamp}.csv"`);
        return res.status(200).send(toCSV(rows));
      }
      return res.status(200).json({ ok: true, total: rows.length, leads: rows });
    }

    if (req.method === 'DELETE') {
      const path = String(req.query.path || '');
      if (!path.startsWith(PREFIX) || path.includes('..')) return res.status(400).json({ ok: false, error: 'Ruta inválida.' });
      await del(path);
      return res.status(200).json({ ok: true });
    }

    res.setHeader('Allow', 'GET, DELETE');
    return res.status(405).json({ ok: false, error: 'Método no permitido.' });
  } catch (err) {
    console.error('leads api failed', err);
    return res.status(500).json({ ok: false, error: 'Error al consultar el almacén.' });
  }
}

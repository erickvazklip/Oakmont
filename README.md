# Oakmont Services — Sitio web

Sitio corporativo de **Oakmont Services**, consultora de tecnologías de la
información. _Architecting Technology Advantage._

- **Páginas:** HTML estático generado por un script de Python (solo librería
  estándar). El HTML generado se versiona, así que el hosting no necesita build.
- **Formulario de contacto:** funciones de Vercel que guardan cada lead en un
  almacén privado (Vercel Blob), con panel de consulta y exportación a CSV.

## Mapa del sitio

| Ruta | Contenido |
|---|---|
| `/` | Inicio |
| `/servicios/` y `/servicios/<servicio>/` | Índice y 8 páginas de detalle |
| `/industrias/` y `/industrias/<industria>/` | Índice y 3 industrias |
| `/casos/` y `/casos/<caso>/` | Índice y 3 casos |
| `/enfoque/` | Horizontes, capa transversal, engagement, gobierno, contratos, métricas |
| `/nosotros/` | Quiénes somos, propósito, principios, talento, alianzas |
| `/diagnostico/` | Diagnóstico estratégico de dos semanas |
| `/contacto/` | Formulario de contacto |
| `/aviso-de-privacidad/` | Aviso de privacidad |
| `/404.html` | Página no encontrada |
| `/admin/` | Panel de leads (no indexable, protegido con contraseña) |

## Estructura del repositorio

```
build/content.py     Todo el texto del sitio (servicios, industrias, casos, enfoque…)
build/build.py       Generador de páginas, sitemap.xml y robots.txt
build/icons.py       Íconos SVG incrustados (Lucide 0.456.0, licencia ISC)
css/styles.css       Hoja de estilos única (tokens, componentes, responsive)
js/main.js           Revelados, menús, formulario de contacto
js/admin.js          Panel de leads
api/contacto.js      POST: valida y guarda un lead
api/leads.js         GET (JSON / CSV) y DELETE de leads, con contraseña
api/_lib.js          Utilidades compartidas del API
tests/               Pruebas del API (npm test)
admin/index.html     Panel de leads
images/              Fotografías e imagen para redes (og.jpg)
```

## Criterios editoriales

- **Idioma:** español, con trato de usted. Se quedan en inglés solo los
  nombres de marca: el lema, los nombres de servicios y los marcos
  Define · Evolve · Deliver y Assess · Design · Execute · Sustain.
- **Veracidad:** sin nombres de clientes, cifras de resultados, año de
  fundación, oficinas, certificaciones ni tiempos de respuesta que no estén
  confirmados. Los casos se publican sin nombre de cliente.
- **Movimiento:** solo lo que refuerza el mensaje. El titular de inicio entra
  una vez, los bloques aparecen una vez (600 ms), el diagrama de horizontes se
  dibuja una vez y la línea del modelo recorre sus fases una vez. Con
  «reducir movimiento» activado todo aparece directamente, y sin JavaScript el
  contenido es visible.
- **Accesibilidad:** WCAG 2.1 AA. El dorado de marca `#A8966F` se usa para
  líneas y acentos; sobre fondos claros, el texto dorado usa `#726445`.

## Editar contenido

```bash
# 1. Edita build/content.py
python3 build/build.py                     # 2. Regenera el sitio
python3 build/build.py --preview /ruta     # (opcional) copia con enlaces a index.html
                                           #  para visores que no resuelven carpetas
```

`css/styles.css`, `js/*.js` y `admin/index.html` se editan directamente.

## Formulario de contacto y leads

- `POST /api/contacto` valida los datos, descarta spam (campo trampa y tiempo
  mínimo de llenado) y guarda cada lead como JSON **privado** en Vercel Blob
  (`leads/AAAA-MM/…json`). Funciona también sin JavaScript.
- `/admin/`: buscar, leer el mensaje, **exportar a CSV** (abre directo en
  Excel) y eliminar un lead (por ejemplo, ante una solicitud de derechos ARCO).
- `GET /api/leads` y `GET /api/leads?format=csv` requieren
  `Authorization: Bearer <ADMIN_PASSWORD>`, para conectar un CRM u hoja de cálculo.
- Pruebas: `npm install && npm test`.

## Despliegue en Vercel

1. **Proyecto:** vercel.com → Add New → Project → importar `erickvazklip/Oakmont`.
   Framework: *Other*; sin comando de build; directorio de salida: raíz.
2. **Almacén:** en el proyecto → Storage → Create → **Blob**, acceso **Private** →
   Connect to project (crea `BLOB_READ_WRITE_TOKEN`).
3. **Contraseña del panel:** Settings → Environment Variables → `ADMIN_PASSWORD`
   (tipo *Sensitive*, entorno Production).
4. **Redeploy** para que las funciones tomen las variables.
5. **Dominio:** Settings → Domains → `oakmontservices.com`.

## Desarrollo local

```bash
python3 -m http.server 8000   # sitio estático en http://localhost:8000
```

El formulario y el panel necesitan las funciones de Vercel (`vercel dev` o el
despliegue).

## Dependencias externas

- Tipografías Cinzel y Montserrat (Google Fonts).
- `@vercel/blob` en las funciones del API.

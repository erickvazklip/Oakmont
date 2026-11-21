# Oakmont Services — Sitio web

Sitio corporativo de **Oakmont Services**, consultora de tecnologías de la
información. _Architecting Technology Advantage._

HTML estático generado por un script de Python (solo librería estándar). El
HTML generado se versiona, así que el hosting no necesita build ni servidor.

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
| `/contacto/` | Contacto por correo electrónico |
| `/aviso-de-privacidad/` | Aviso de privacidad |
| `/404.html` | Página no encontrada |

## Estructura del repositorio

```
build/content.py     Todo el texto del sitio (servicios, industrias, casos, enfoque…)
build/build.py       Generador de páginas, sitemap.xml y robots.txt
build/icons.py       Íconos SVG incrustados (Lucide 0.456.0, licencia ISC)
build/diagrams.py    Diagramas alegóricos de servicios, industrias y enfoque
css/styles.css       Hoja de estilos única (tokens, componentes, responsive)
js/main.js           Revelados, menús desplegables y menú móvil
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
  una vez, los bloques aparecen una vez (600 ms) y la línea del modelo recorre
  sus fases una vez. Cada servicio, cada industria y el enfoque tienen un
  diagrama alegórico (`build/diagrams.py`) que explica su idea mientras se
  dibuja, una sola vez y en el orden del mensaje. Con
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

`css/styles.css` y `js/main.js` se editan directamente.

## Publicación

Es un sitio estático: sirve en cualquier hosting (Vercel, Netlify, Cloudflare
Pages, GitHub Pages con dominio propio). En Vercel: Add New → Project →
importar `erickvazklip/Oakmont`, framework *Other*, sin comando de build,
directorio de salida la raíz; después, Settings → Domains → `oakmontservices.com`.
Publicar en la raíz del dominio (la página 404 usa rutas absolutas).

## Pendiente antes de producción

1. **Datos legales del aviso de privacidad:** completar `legal_name` y
   `legal_address` en `SITE` (`build/content.py`) y regenerar. Mientras falten,
   `build.py` lo advierte en cada ejecución. Conviene una revisión legal del texto.
2. **Publicación:** pasos en «Publicación».

## Desarrollo local

```bash
python3 -m http.server 8000   # http://localhost:8000
```

## Dependencias externas

- Tipografías Cinzel y Montserrat (Google Fonts).

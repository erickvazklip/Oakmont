# Oakmont Services — Sitio web

Sitio corporativo de **Oakmont Services**, consultora de TI.
_Architecting Technology Advantage._

HTML estático, sin framework. El contenido vive en un solo archivo de datos y un
script de Python (solo librería estándar) genera las páginas. El HTML generado se
versiona, así que el hosting no necesita paso de build.

## Mapa del sitio

```
/                                   Inicio
/servicios/                         Índice de servicios
/servicios/<servicio>/              8 páginas de detalle
/industrias/                        Índice de industrias
/industrias/<industria>/            3 páginas de detalle
/casos/                             Índice de casos
/casos/<caso>/                      3 casos detallados
/enfoque/                           Framework, engagement, gobierno, contratos
/nosotros/                          Quiénes somos, principios, talento
/diagnostico/                       Diagnóstico estratégico de dos semanas
/contacto/                          Formulario de contacto
/aviso-de-privacidad/               Aviso de privacidad
/404.html                           Página no encontrada
sitemap.xml · robots.txt · favicon.svg · images/og.jpg
```

## Editar contenido

1. Edita `build/content.py` (servicios, industrias, casos, enfoque, datos del sitio).
2. Regenera: `python3 build/build.py`
3. Revisa localmente y haz commit de los archivos generados.

`css/styles.css` y `js/main.js` se editan directamente.

## Antes de publicar

- **Aviso de privacidad:** completar `legal_name` y `legal_address` en `SITE`
  (`build/content.py`) y regenerar.
- **Dominio:** `SITE["domain"]` se usa en canonical, Open Graph y `sitemap.xml`.
- **LinkedIn:** confirmar la URL en `SITE["linkedin"]`.
- **Formulario:** hoy abre el cliente de correo del visitante con el mensaje
  listo (`mailto:`). Para recibir envíos directamente, conectar un servicio de
  formularios (p. ej. Formspree o Netlify Forms) y cambiar el `action` del
  formulario en `build_contact()`.
- **Hosting:** publicar en la raíz de un dominio (la 404 usa rutas absolutas).

## Desarrollo local

```bash
python3 -m http.server 8000
```

Abre <http://localhost:8000>. Ábrelo a través de un servidor (no con `file://`)
para que funcionen las rutas de carpetas.

## Movimiento

Solo se anima lo que refuerza el discurso: entrada del titular, diagrama de
horizontes que se dibuja una vez, línea que recorre las fases del modelo y
apariciones breves de cada bloque. Con `prefers-reduced-motion` todo aparece
directamente, y sin JS el contenido es visible.

## Dependencias externas

- Tipografías: Cinzel y Montserrat (Google Fonts).
- Íconos: Lucide 0.456.0 (unpkg).

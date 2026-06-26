# Oakmont Services — Página principal

Landing page estática (one-pager) de **Oakmont Services**, consultora de TI.
_Architecting Technology Advantage._

Sin framework, sin paso de build: HTML, CSS y un único archivo JS.

## Estructura

```
.
├── index.html        # Página principal
├── css/
│   └── styles.css    # Design system (tokens + componentes) + estilos de página
├── js/
│   └── main.js       # Scroll reveals, header sticky, parallax, hover, iconos
└── images/           # Imágenes del sitio (signage, stairs, reception, meeting, globe, wave)
```

## Desarrollo local

No requiere instalación. Sirve la carpeta con cualquier servidor estático:

```bash
python3 -m http.server 8000
# o
npx serve .
```

Luego abre <http://localhost:8000>.

> Nota: ábrelo a través de un servidor (no con `file://`) para que se carguen
> correctamente las rutas relativas de CSS, JS e imágenes.

## Dependencias externas (vía CDN)

- **Tipografías:** [Cinzel](https://fonts.google.com/specimen/Cinzel) y
  [Montserrat](https://fonts.google.com/specimen/Montserrat) (Google Fonts).
- **Iconos:** [Lucide](https://lucide.dev) (`unpkg`).

## Despliegue

Compatible con cualquier hosting estático: GitHub Pages, Netlify, Vercel o
Cloudflare Pages. Basta con publicar la raíz del repositorio.

## Origen

Diseñado en Claude Design y exportado a HTML/CSS/JS estándar, eliminando el
runtime del editor y las dependencias propietarias.

# Oakmont Services — Página principal

Landing page estática (one-pager) de **Oakmont Services**, consultora de TI.
_Architecting Technology Advantage._

Sin framework, sin paso de build: HTML, CSS y un único archivo JS.

## Estructura

```
.
├── index.html        # Página principal
├── css/
│   └── styles.css    # Tokens de marca + capa de experiencia (escenas, motion, responsive)
├── js/
│   └── main.js       # Motor de escenas sin dependencias (scroll, reveals, canvas, menú)
└── images/           # Imágenes del sitio (signage, stairs, reception, meeting, globe, wave)
```

## Experiencia

Narrativa por escenas ligadas al scroll. Lenguaje de motion: *luz que recorre piedra*
(revelados por máscara, lentos y precisos).

| Escena | Comportamiento |
|---|---|
| Hero | Fijo; el titular se disuelve y el letrero avanza al desplazar. Retícula de puntos en canvas que se ilumina con el cursor |
| Manifiesto | La frase se ilumina palabra por palabra al ritmo del scroll |
| Visión | Tres fuerzas con revelado escalonado |
| Value at stake | Una ventana (clip-path) se abre hasta cubrir la pantalla |
| Enfoque | Split editorial con imagen en parallax y pilares |
| Framework | Scroll fijo: Define / Evolve / Deliver encienden un diagrama de horizontes |
| Capacidades | Bento de 8 capacidades con luz que sigue al cursor |
| Modelo | Recorrido horizontal fijo (desktop) / swipe con snap (móvil) |
| Cifras · Razones · Casos | Revelado por máscara, filas con trazo dorado, tarjetas apiladas |
| CTA | Botón magnético |

Todo el movimiento lo controla una sola variable CSS (`--p`, 0 → 1) que escribe
`js/main.js` en un único `requestAnimationFrame`. Solo se animan `transform`,
`opacity`, `filter` y `clip-path`. Con `prefers-reduced-motion` todas las escenas
se resuelven a su estado final legible, y sin JS el contenido es visible.

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

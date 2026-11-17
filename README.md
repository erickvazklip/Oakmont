# Oakmont Services — Página principal

Landing page estática (one-pager) de **Oakmont Services**, consultora de TI.
_Architecting Technology Advantage._

Sin framework, sin paso de build: HTML, CSS y un único archivo JS.

## Estructura

```
.
├── index.html        # Página principal
├── css/
│   └── styles.css    # Tokens de marca + estilos de página y responsive
├── js/
│   └── main.js       # Revelados únicos, header, sección activa y menú móvil
└── images/           # Imágenes del sitio (signage, stairs, reception, meeting, globe, wave)
```

## Experiencia

Movimiento mínimo y con intención: solo se anima lo que refuerza el discurso.

| Animación | Qué comunica |
|---|---|
| Entrada del titular al cargar (una vez) | Presenta la marca |
| Diagrama de horizontes que se dibuja de adentro hacia afuera | Define → Evolve → Deliver, todo dentro de un mismo gobierno |
| Línea dorada que recorre Assess → Sustain | Un solo responsable de principio a fin |
| Aparición breve de cada bloque (600 ms, 16 px) | Ritmo de lectura |

Sin pines de scroll, parallax, scroll horizontal ni animaciones infinitas. Con
`prefers-reduced-motion` todo aparece directamente, y sin JS el contenido es visible.

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

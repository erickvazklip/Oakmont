# -*- coding: utf-8 -*-
"""
Oakmont Services — static site generator.

    python3 build/build.py

Reads build/content.py and writes plain HTML into the repository root
(index.html, servicios/..., industrias/..., casos/..., etc.), plus
sitemap.xml and robots.txt. No dependencies beyond the Python stdlib.
The generated files are committed, so hosting needs no build step.
"""
import json
import os
import sys
from html import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content as C  # noqa: E402

SVC = {s["slug"]: s for s in C.SERVICES}
IND = {i["slug"]: i for i in C.INDUSTRIES}
CASE = {c["slug"]: c for c in C.CASES}
PAGES = []  # for sitemap


def e(s):
    return escape(s, quote=True)


def icon(name):
    return f'<i data-lucide="{name}" aria-hidden="true"></i>'


# --------------------------------------------------------------------------
# Shared chrome
# --------------------------------------------------------------------------
def header(r, active, home):
    core = [s for s in C.SERVICES if s["plane"] == "nucleo"]
    enab = [s for s in C.SERVICES if s["plane"] == "habilitadora"]

    def mm_list(items):
        return "".join(
            f'<li><a href="{r}servicios/{s["slug"]}/"><strong>{e(s["name"])}</strong><span>{e(s["short"])}</span></a></li>'
            for s in items)

    ind_list = "".join(f'<li><a href="{r}industrias/{i["slug"]}/">{e(i["name"])}</a></li>' for i in C.INDUSTRIES)

    def cls(key):
        return ' class="is-current" aria-current="page"' if active == key else ""

    return f'''
<a class="skip" href="#contenido">Saltar al contenido</a>
<header class="nav{'' if home else ' is-solid nav--static'}" id="nav">
  <div class="nav__inner">
    <a href="{r}" class="wordmark" aria-label="Oakmont Services — inicio">
      <span class="wordmark__name">OAKMONT</span>
      <span class="wordmark__sub">SERVICES</span>
    </a>
    <nav class="nav__links" aria-label="Principal">
      <div class="nav__item has-menu">
        <a href="{r}servicios/"{cls("servicios")}>Servicios</a>
        <button class="nav__caret" aria-expanded="false" aria-controls="mm-servicios" aria-label="Mostrar servicios"><svg viewBox="0 0 12 12" aria-hidden="true"><path d="M3 4.5 6 7.5 9 4.5" fill="none" stroke="currentColor" stroke-width="1.4"/></svg></button>
        <div class="mega" id="mm-servicios">
          <div class="mega__inner">
            <div class="mega__col"><p class="mega__h">Capacidades núcleo</p><ul>{mm_list(core)}</ul></div>
            <div class="mega__col"><p class="mega__h">Capacidades habilitadoras</p><ul>{mm_list(enab)}</ul></div>
            <div class="mega__aside">
              <p class="mega__h">Empiece aquí</p>
              <a class="mega__feature" href="{r}diagnostico/"><strong>Diagnóstico estratégico de dos semanas</strong><span>Hallazgos accionables y prioridades claras, sin compromiso.</span></a>
              <a class="mega__all" href="{r}servicios/">Ver todos los servicios</a>
            </div>
          </div>
        </div>
      </div>
      <div class="nav__item has-menu">
        <a href="{r}industrias/"{cls("industrias")}>Industrias</a>
        <button class="nav__caret" aria-expanded="false" aria-controls="mm-industrias" aria-label="Mostrar industrias"><svg viewBox="0 0 12 12" aria-hidden="true"><path d="M3 4.5 6 7.5 9 4.5" fill="none" stroke="currentColor" stroke-width="1.4"/></svg></button>
        <div class="drop" id="mm-industrias"><ul>{ind_list}<li><a class="drop__all" href="{r}industrias/">Todas las industrias</a></li></ul></div>
      </div>
      <div class="nav__item"><a href="{r}enfoque/"{cls("enfoque")}>Enfoque</a></div>
      <div class="nav__item"><a href="{r}casos/"{cls("casos")}>Casos</a></div>
      <div class="nav__item"><a href="{r}nosotros/"{cls("nosotros")}>Nosotros</a></div>
    </nav>
    <a href="{r}diagnostico/" class="btn btn--gold btn--sm nav__cta">Agendar diagnóstico</a>
    <button class="nav__toggle" aria-expanded="false" aria-controls="menu" aria-label="Abrir menú"><span></span><span></span></button>
  </div>
</header>

<div class="menu" id="menu" hidden>
  <nav aria-label="Menú móvil">
    <details><summary>Servicios</summary><ul>
      <li><a href="{r}servicios/">Todos los servicios</a></li>
      {"".join(f'<li><a href="{r}servicios/{s["slug"]}/">{e(s["name"])}</a></li>' for s in C.SERVICES)}
    </ul></details>
    <details><summary>Industrias</summary><ul>
      <li><a href="{r}industrias/">Todas las industrias</a></li>
      {"".join(f'<li><a href="{r}industrias/{i["slug"]}/">{e(i["name"])}</a></li>' for i in C.INDUSTRIES)}
    </ul></details>
    <a href="{r}enfoque/">Enfoque</a>
    <a href="{r}casos/">Casos</a>
    <a href="{r}nosotros/">Nosotros</a>
    <a href="{r}contacto/">Contacto</a>
    <a class="btn btn--gold btn--lg" href="{r}diagnostico/">Agendar diagnóstico</a>
  </nav>
</div>
'''


def footer(r):
    svc = "".join(f'<a href="{r}servicios/{s["slug"]}/">{e(s["name"])}</a>' for s in C.SERVICES)
    ind = "".join(f'<a href="{r}industrias/{i["slug"]}/">{e(i["name"])}</a>' for i in C.INDUSTRIES)
    return f'''
<footer class="footer">
  <div class="container footer__top">
    <div class="footer__brand">
      <a href="{r}" class="wordmark wordmark--lg" aria-label="Oakmont Services — inicio">
        <span class="wordmark__name">OAKMONT</span>
        <span class="wordmark__sub">SERVICES</span>
      </a>
      <p class="footer__tag">Architecting Technology Advantage</p>
      <p class="footer__pitch">Consultoría en tecnologías de la información: estrategia, arquitectura e ingeniería bajo un modelo de gobierno único.</p>
    </div>
    <div class="footer__cols">
      <nav aria-label="Servicios"><h4>Servicios</h4>{svc}</nav>
      <nav aria-label="Industrias"><h4>Industrias</h4>{ind}</nav>
      <nav aria-label="Firma"><h4>Firma</h4>
        <a href="{r}enfoque/">Enfoque</a><a href="{r}casos/">Casos</a><a href="{r}nosotros/">Nosotros</a>
        <a href="{r}diagnostico/">Diagnóstico</a><a href="{r}contacto/">Contacto</a>
      </nav>
      <div><h4>Contacto</h4>
        <a href="mailto:{C.SITE["email"]}">{C.SITE["email"]}</a>
        <a href="{C.SITE["linkedin"]}" rel="noopener" target="_blank">LinkedIn</a>
      </div>
    </div>
  </div>
  <div class="container footer__bottom">
    <span>© 2026 Oakmont Services. Todos los derechos reservados.</span>
    <a href="{r}aviso-de-privacidad/">Aviso de privacidad</a>
  </div>
</footer>
'''


def crumbs_html(r, crumbs):
    items = [f'<li><a href="{r}">Inicio</a></li>']
    for i, (label, href) in enumerate(crumbs):
        if i == len(crumbs) - 1:
            items.append(f'<li aria-current="page">{e(label)}</li>')
        else:
            items.append(f'<li><a href="{r}{href}">{e(label)}</a></li>')
    return f'<nav class="crumbs" aria-label="Ruta de navegación"><ol>{"".join(items)}</ol></nav>'


def crumbs_ld(crumbs):
    items = [{"@type": "ListItem", "position": 1, "name": "Inicio", "item": C.SITE["domain"] + "/"}]
    for i, (label, href) in enumerate(crumbs):
        items.append({"@type": "ListItem", "position": i + 2, "name": label, "item": C.SITE["domain"] + "/" + href})
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}


def write(path, title, desc, body, active="", crumbs=None, home=False, ld=None, r=None):
    """path: output path relative to ROOT, e.g. 'servicios/x/index.html'."""
    depth = path.count("/")
    if r is None:
        r = "../" * depth
    url_path = "" if path == "index.html" else path.replace("index.html", "")
    canonical = C.SITE["domain"] + "/" + url_path
    full_title = title if home else f"{title} | Oakmont Services"
    lds = list(ld or [])
    if crumbs:
        lds.append(crumbs_ld(crumbs))
    ld_html = "".join(
        f'\n  <script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in lds)
    html = f'''<!DOCTYPE html>
<html lang="es" class="no-js">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(full_title)}</title>
  <meta name="description" content="{e(desc)}">
  <link rel="canonical" href="{canonical}">
  <meta name="theme-color" content="#141414">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Oakmont Services">
  <meta property="og:locale" content="es_MX">
  <meta property="og:title" content="{e(full_title)}">
  <meta property="og:description" content="{e(desc)}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{C.SITE["domain"]}/images/og.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="{r}favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400&family=Montserrat:wght@300;400;500;600&display=swap">
  <link rel="stylesheet" href="{r}css/styles.css">
  <script>document.documentElement.classList.replace('no-js','js');</script>
  <script src="https://unpkg.com/lucide@0.456.0/dist/umd/lucide.min.js" defer></script>
  <script src="{r}js/main.js" defer></script>{ld_html}
</head>
<body{' class="is-home"' if home else ''}>
{header(r, active, home)}
<main id="contenido">
{body}
</main>
{footer(r)}
</body>
</html>
'''
    out = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    if path != "404.html":
        PAGES.append(url_path)


# --------------------------------------------------------------------------
# Reusable blocks
# --------------------------------------------------------------------------
def phero(r, crumbs, label, title, lede, actions="", extra_cls=""):
    return f'''
<section class="phero {extra_cls}">
  <div class="container">
    {crumbs_html(r, crumbs)}
    <p class="label rv">{e(label)}</p>
    <h1 class="phero__title rv">{e(title)}</h1>
    <p class="phero__lede rv">{e(lede)}</p>
    {actions}
  </div>
</section>'''


def head(label, title, dark=False, aside=""):
    lab = "label" if dark else "label label--dark"
    disp = "display display--light" if dark else "display"
    a = f'<p class="head__aside">{e(aside)}</p>' if aside else ""
    return f'''<header class="head{' head--row' if aside else ''} rv"><div><p class="{lab}">{e(label)}</p><h2 class="{disp}">{e(title)}</h2></div>{a}</header>'''


def cta_band(r, title="Empecemos por entender dónde está hoy su tecnología.",
             text="Un diagnóstico estratégico de dos semanas, sin compromiso, con hallazgos accionables."):
    return f'''
<section class="ctaband">
  <div class="container ctaband__inner rv">
    <div>
      <h2 class="ctaband__title">{e(title)}</h2>
      <p>{e(text)}</p>
    </div>
    <div class="ctaband__actions">
      <a href="{r}diagnostico/" class="btn btn--gold btn--lg">Agendar diagnóstico</a>
      <a href="{r}contacto/" class="link-arrow">Contactar a Oakmont</a>
    </div>
  </div>
</section>'''


def svc_card(r, s):
    return f'''<a class="scard rv" href="{r}servicios/{s["slug"]}/">
  {icon(s["icon"])}
  <h3>{e(s["name"])}</h3>
  <p class="scard__en">{e(s["en"])}</p>
  <p>{e(s["short"])}</p>
  <span class="scard__more">Ver servicio</span>
</a>'''


def phases(items):
    lis = "".join(
        f'<li><span class="phases__dot" aria-hidden="true"></span><span class="phases__n">{i+1:02d}</span><h3>{e(t)}</h3><p>{e(d)}</p></li>'
        for i, (t, d) in enumerate(items))
    return f'<ol class="phases rv">{lis}</ol>'


# --------------------------------------------------------------------------
# Pages
# --------------------------------------------------------------------------
def build_home():
    r = ""
    core = [s for s in C.SERVICES if s["plane"] == "nucleo"]
    enab = [s for s in C.SERVICES if s["plane"] == "habilitadora"]

    def tile(s, extra=""):
        chips = ""
        if s["slug"] == "cloud-multicloud":
            chips = '<ul class="tile__chips" aria-label="Marco 7R">' + "".join(f"<li>{x}</li>" for x, _ in s["seven_r"]) + "</ul>"
        img = ""
        if "tile--hero" in extra:
            img = '<div class="tile__img" aria-hidden="true"><img src="images/meeting.jpg" alt="" width="1536" height="1024" loading="lazy"></div>'
        return f'''<a class="tile {extra} rv" href="servicios/{s["slug"]}/">{img}
        {icon(s["icon"])}
        <h3>{e(s["name"])}</h3>
        <p class="tile__en">{e(s["en"])}</p>
        <p>{e(s["short"])}</p>{chips}
        <span class="tile__more">Ver servicio</span>
      </a>'''

    bento = tile(core[0], "tile--hero") + tile(core[1]) + tile(core[2]) + tile(core[3], "tile--wide tile--dark")
    enablers = "".join(tile(s, "tile--flat") for s in enab)

    inds = "".join(f'''<a class="icard rv" href="industrias/{i["slug"]}/">
        {icon(i["icon"])}<h3>{e(i["name"])}</h3><p>{e(i["tagline"])}</p><span class="scard__more">Ver industria</span></a>''' for i in C.INDUSTRIES)

    cases = "".join(f'''<a class="case rv" href="casos/{c["slug"]}/">
        <p class="case__meta">Caso {c["n"]} · {e(IND[c["industry"]]["name"])}</p>
        <h3 class="case__result">{e(c["title"])}</h3>
        <p class="case__sum">{e(c["summary"])}</p>
        <span class="scard__more">Leer el caso</span>
      </a>''' for c in C.CASES)

    reasons = "".join(f'<li><span>{n}</span><h3>{e(t)}</h3><p>{e(d.split(". ")[0])}.</p></li>' for n, t, d in C.REASONS)

    body = f'''
<section class="hero" id="top" aria-label="Introducción">
  <div class="hero__media" aria-hidden="true"><img src="images/signage.jpg" alt="" width="554" height="474" fetchpriority="high"></div>
  <div class="hero__veil" aria-hidden="true"></div>
  <div class="hero__content container">
    <p class="kicker rv">Consultoría en tecnologías de la información</p>
    <h1 class="hero__title lines" aria-label="Architecting Technology Advantage">
      <span><span>Architecting</span></span>
      <span><span>Technology</span></span>
      <span><span class="gold">Advantage</span></span>
    </h1>
    <p class="hero__lede rv" style="--d:.5s">Acompañamos a la dirección ejecutiva en la definición, evolución e ingeniería de soluciones tecnológicas — de la estrategia a la producción, bajo un modelo de gobierno único.</p>
    <div class="hero__actions rv" style="--d:.6s">
      <a href="diagnostico/" class="btn btn--gold btn--lg">Agendar diagnóstico</a>
      <a href="servicios/" class="link-arrow">Explorar servicios {icon("arrow-right")}</a>
    </div>
  </div>
</section>

<section class="manifesto" aria-label="Nuestra convicción">
  <div class="container">
    <p class="label rv">Nuestra convicción</p>
    <p class="manifesto__text rv">El valor no proviene de adoptar tecnología, sino de orquestar <em>estrategia, arquitectura y ejecución</em> como un sistema único.</p>
  </div>
</section>

<section class="section section--light">
  <div class="container">
    {head("Punto de vista", "Una reconfiguración estructural redefine la economía de cada industria.")}
    <ol class="forces" data-stagger>
      <li class="force rv"><span class="force__n">01</span><h3>Erosión de la deuda tecnológica</h3><p>El mantenimiento del legado absorbe una parte desproporcionada del presupuesto de TI y frena la capacidad de innovar.</p></li>
      <li class="force rv"><span class="force__n">02</span><h3>Tensión velocidad&nbsp;– control</h3><p>El negocio exige entregar más rápido sin comprometer calidad, seguridad ni cumplimiento.</p></li>
      <li class="force rv"><span class="force__n">03</span><h3>Escasez estructural de talento</h3><p>La demanda de capacidades críticas supera de forma persistente a la oferta disponible.</p></li>
    </ol>
  </div>
</section>

<section class="stake" aria-labelledby="stake-title">
  <div class="stake__bg" aria-hidden="true"><img src="images/stairs.jpg" alt="" width="398" height="474" loading="lazy"></div>
  <div class="container stake__content">
    <header class="rv"><p class="label">Value at stake</p><h2 class="display display--light" id="stake-title">El costo silencioso de no evolucionar.</h2></header>
    <div class="stake__grid" data-stagger>
      <div class="rv"><h3>Crecimiento</h3><p>Ingresos no capturados por time-to-market lento y experiencias digitales rezagadas.</p></div>
      <div class="rv"><h3>Eficiencia</h3><p>Sobrecosto operativo del legado y de infraestructura sobredimensionada que drena la inversión disponible.</p></div>
      <div class="rv"><h3>Riesgo</h3><p>Exposición a interrupciones, brechas de seguridad e incumplimiento regulatorio.</p></div>
    </div>
    <p class="stake__close rv">Cada trimestre de inacción es valor que se transfiere a la competencia.</p>
  </div>
</section>

<section class="section section--ivory" id="capacidades">
  <div class="container">
    {head("Servicios", "Un portafolio modular en dos planos.", aside="Cuatro capacidades núcleo que construyen. Cuatro habilitadoras que aseguran que lo construido sea seguro, confiable y medible.")}
    <p class="plane rv">Capacidades núcleo</p>
    <div class="bento" data-stagger>{bento}</div>
    <p class="plane rv">Capacidades habilitadoras</p>
    <div class="enablers" data-stagger>{enablers}</div>
    <p class="more rv"><a class="link-arrow link-arrow--dark" href="servicios/">Ver todos los servicios {icon("arrow-right")}</a></p>
  </div>
</section>

<section class="framework" aria-labelledby="fw-title">
  <div class="container">
    <header class="head rv"><p class="label">Enfoque</p><h2 class="display display--light" id="fw-title">Tres horizontes, un solo gobierno.</h2></header>
    <div class="framework__grid">
      {orbit_svg()}
      <ol class="horizons" data-stagger>
        {"".join(f'<li class="rv"><span class="horizons__n">{n}</span><div><h3>{t}</h3><p class="horizons__sub">{e(sub)}</p><p>{e(d)}</p></div></li>' for n, t, sub, d, _ in C.HORIZONS)}
      </ol>
    </div>
    <p class="more rv"><a class="link-arrow" href="enfoque/">Conocer el enfoque completo {icon("arrow-right")}</a></p>
  </div>
</section>

<section class="section section--paper">
  <div class="container">
    {head("Industrias", "Experiencia en sectores donde la tecnología es el negocio.")}
    <div class="icards" data-stagger>{inds}</div>
  </div>
</section>

<section class="figures" aria-label="Oakmont en cifras">
  <div class="container figures__grid rv">
    <div class="figure"><strong>2</strong><span>semanas de diagnóstico estratégico, con hallazgos accionables</span></div>
    <div class="figure"><strong>8</strong><span>capacidades integradas en un solo portafolio</span></div>
    <div class="figure"><strong>3</strong><span>hyperscalers: AWS, Microsoft Azure y Google Cloud</span></div>
    <div class="figure"><strong>1</strong><span>responsable de la estrategia a la operación</span></div>
  </div>
</section>

<section class="why" aria-labelledby="why-title">
  <div class="why__bg" aria-hidden="true"><img src="images/globe.jpg" alt="" width="532" height="474" loading="lazy"></div>
  <div class="container">
    <header class="head rv"><p class="label">Por qué Oakmont</p><h2 class="display display--light" id="why-title">Cinco razones para confiar la decisión.</h2></header>
    <ol class="reasons rv">{reasons}</ol>
    <p class="more rv"><a class="link-arrow" href="nosotros/">Conocer a Oakmont {icon("arrow-right")}</a></p>
  </div>
</section>

<section class="section section--paper">
  <div class="container">
    <header class="head head--row rv">
      <div><p class="label label--dark">Credentials &amp; proof points</p><h2 class="display">Casos representativos e impacto.</h2></div>
      <ul class="partners" aria-label="Alianzas"><li>AWS</li><li>Microsoft Azure</li><li>Google Cloud</li></ul>
    </header>
    <div class="cases" data-stagger>{cases}</div>
  </div>
</section>

<section class="cta" aria-labelledby="cta-title">
  <div class="cta__bg" aria-hidden="true"><img src="images/wave.jpg" alt="" width="342" height="523" loading="lazy"></div>
  <div class="container cta__inner rv">
    <p class="label">Siguiente paso</p>
    <h2 class="cta__title" id="cta-title">La distancia entre la ambición tecnológica y su ejecución es donde se gana la ventaja.</h2>
    <p class="cta__sub">Oakmont existe para cerrarla. Propongamos un diagnóstico estratégico de dos semanas — sin compromiso, con hallazgos accionables.</p>
    <div class="cta__actions">
      <a href="diagnostico/" class="btn btn--gold btn--lg">Agendar diagnóstico</a>
      <a href="contacto/" class="link-arrow">Contactar a Oakmont</a>
    </div>
  </div>
</section>'''
    org = {
        "@context": "https://schema.org", "@type": "Organization",
        "name": C.SITE["name"], "url": C.SITE["domain"] + "/", "email": C.SITE["email"],
        "slogan": C.SITE["tagline"], "description": C.SITE["description"],
        "logo": C.SITE["domain"] + "/favicon.svg", "sameAs": [C.SITE["linkedin"]],
    }
    write("index.html", "Oakmont Services — Architecting Technology Advantage", C.SITE["description"],
          body, home=True, ld=[org])


def orbit_svg():
    return '''<figure class="orbit-wrap rv">
        <svg class="orbit" viewBox="0 0 400 400" role="img" aria-label="Tres horizontes concéntricos — Define, Evolve y Deliver — dentro de una misma capa de gobierno">
          <circle class="orbit__gov" cx="200" cy="200" r="190" pathLength="1"/>
          <circle class="orbit__ring r3" cx="200" cy="200" r="150" pathLength="1"/>
          <circle class="orbit__ring r2" cx="200" cy="200" r="104" pathLength="1"/>
          <circle class="orbit__ring r1" cx="200" cy="200" r="58" pathLength="1"/>
          <circle class="orbit__core" cx="200" cy="200" r="5"/>
          <text class="t1" x="200" y="204">DEFINE</text>
          <text class="t2" x="200" y="116">EVOLVE</text>
          <text class="t3" x="200" y="70">DELIVER</text>
          <text class="t4" x="200" y="24">GOBIERNO</text>
        </svg>
        <figcaption><span>Capa transversal</span><ul><li>Governance</li><li>Quality</li><li>Security</li><li>Innovation</li></ul></figcaption>
      </figure>'''


def build_services_index():
    r = "../"
    crumbs = [("Servicios", "servicios/")]
    core = "".join(svc_card(r, s) for s in C.SERVICES if s["plane"] == "nucleo")
    enab = "".join(svc_card(r, s) for s in C.SERVICES if s["plane"] == "habilitadora")
    body = phero(r, crumbs, "Servicios", "Un portafolio modular en dos planos.",
                 "Cuatro capacidades núcleo que construyen y cuatro habilitadoras que aseguran que lo construido sea seguro, confiable y medible. Se contratan por separado o como un solo programa bajo el mismo gobierno.") + f'''
<section class="section section--paper">
  <div class="container">
    {head("Capacidades núcleo", "Lo que construye.")}
    <div class="scards" data-stagger>{core}</div>
  </div>
</section>
<section class="section section--ivory">
  <div class="container">
    {head("Capacidades habilitadoras", "Lo que asegura que funcione.")}
    <div class="scards" data-stagger>{enab}</div>
  </div>
</section>
<section class="section section--light">
  <div class="container split split--even">
    <div class="rv">
      <p class="label label--dark">Cómo se combinan</p>
      <h2 class="display">Un solo programa, un solo responsable.</h2>
    </div>
    <div class="rv">
      <p class="lede">La mayoría de las iniciativas combina varias capacidades: una modernización a la nube necesita estrategia, ingeniería, seguridad, calidad y operación.</p>
      <p class="lede">En Oakmont todas responden al mismo gobierno de entrega, con un único punto de responsabilidad y un mismo tablero de indicadores.</p>
      <p class="more"><a class="link-arrow link-arrow--dark" href="{r}enfoque/">Ver cómo trabajamos {icon("arrow-right")}</a></p>
    </div>
  </div>
</section>''' + cta_band(r)
    write("servicios/index.html", "Servicios", "Ocho capacidades de consultoría en TI: fábrica de software, estrategia, talento, nube, datos e IA, ciberseguridad, operación cloud y calidad.",
          body, active="servicios", crumbs=crumbs)


def build_service(s):
    r = "../../"
    crumbs = [("Servicios", "servicios/"), (s["name"], f'servicios/{s["slug"]}/')]
    plane = "Capacidad núcleo" if s["plane"] == "nucleo" else "Capacidad habilitadora"
    actions = f'''<div class="phero__actions rv"><a href="{r}contacto/?interes={s["slug"]}" class="btn btn--gold btn--lg">Hablar con un especialista</a><a href="#que-hacemos" class="link-arrow">Qué hacemos</a></div>'''
    problems = "".join(f'<li class="rv"><h3>{e(t)}</h3><p>{e(d)}</p></li>' for t, d in s["problems"])
    offerings = "".join(f'<li class="rv"><span class="offer__n">{i+1:02d}</span><div><h3>{e(t)}</h3><p>{e(d)}</p></div></li>' for i, (t, d) in enumerate(s["offerings"]))
    seven = ""
    if s.get("seven_r"):
        seven = f'''
<section class="section section--light">
  <div class="container">
    {head("Marco 7R", "Siete decisiones posibles para cada aplicación.")}
    <ol class="sevenr rv">{"".join(f'<li><strong>{e(n)}</strong><span>{e(d)}</span></li>' for n, d in s["seven_r"])}</ol>
  </div>
</section>'''
    deliv = "".join(f'<li>{icon("check")}<span>{e(d)}</span></li>' for d in s["deliverables"])
    models = "".join(f'<li>{e(m)}</li>' for m in s["models"])
    outcomes = "".join(f'<li class="rv"><h3>{e(t)}</h3><p>{e(d)}</p></li>' for t, d in s["outcomes"])
    faqs = "".join(f'<details class="faq__item"><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in s["faqs"])
    related = "".join(svc_card(r, SVC[x]) for x in s["related"])
    inds = [i for i in C.INDUSTRIES if any(h[0] == s["slug"] for h in i["help"])]
    ind_links = ""
    if inds:
        ind_links = '<p class="aside__h">Industrias</p><ul>' + "".join(f'<li><a href="{r}industrias/{i["slug"]}/">{e(i["name"])}</a></li>' for i in inds) + "</ul>"
    cases = [c for c in C.CASES if s["slug"] in c["services"]]
    case_links = ""
    if cases:
        case_links = '<p class="aside__h">Casos relacionados</p><ul>' + "".join(f'<li><a href="{r}casos/{c["slug"]}/">{e(c["title"])}</a></li>' for c in cases) + "</ul>"

    body = phero(r, crumbs, f'{plane} · {s["en"]}', s["name"], s["lede"], actions) + f'''
<section class="section section--paper">
  <div class="container">
    <div class="svc-intro rv">
      <p class="svc-intro__tag">{e(s["tagline"])}</p>
    </div>
    {head("Cuándo nos llaman", "Señales de que este servicio es para usted.")}
    <ul class="problems">{problems}</ul>
  </div>
</section>

<section class="section section--light" id="que-hacemos">
  <div class="container with-aside">
    <div>
      {head("Qué hacemos", "Alcance del servicio.")}
      <ol class="offers">{offerings}</ol>
    </div>
    <aside class="aside rv" aria-label="Relacionado">
      <p class="aside__h">Modelos de contratación</p>
      <ul class="aside__models">{models}</ul>
      {ind_links}
      {case_links}
      <a class="btn btn--dark btn--sm" href="{r}contacto/?interes={s["slug"]}">Solicitar propuesta</a>
    </aside>
  </div>
</section>
{seven}
<section class="framework">
  <div class="container">
    {head("Cómo trabajamos", "Un proceso claro, de principio a fin.", dark=True)}
    {phases(s["approach"])}
  </div>
</section>

<section class="section section--paper">
  <div class="container split split--even">
    <div class="rv">
      <p class="label label--dark">Entregables</p>
      <h2 class="display">Lo que usted recibe.</h2>
    </div>
    <ul class="checklist rv">{deliv}</ul>
  </div>
</section>

<section class="section section--ivory">
  <div class="container">
    {head("Resultados esperados", "Qué cambia en su organización.")}
    <ul class="outcomes" data-stagger>{outcomes}</ul>
  </div>
</section>

<section class="section section--light">
  <div class="container split split--even">
    <div class="rv"><p class="label label--dark">Preguntas frecuentes</p><h2 class="display">Lo que suelen preguntarnos.</h2></div>
    <div class="faq rv">{faqs}</div>
  </div>
</section>

<section class="section section--paper">
  <div class="container">
    {head("Servicios relacionados", "Se combinan bien con este servicio.")}
    <div class="scards scards--3" data-stagger>{related}</div>
  </div>
</section>''' + cta_band(r, title=f'¿Conversamos sobre {s["name"]}?',
                          text="Cuéntenos su contexto y le proponemos el alcance y el modelo de contratación adecuados.")
    ld = [
        {"@context": "https://schema.org", "@type": "Service", "name": s["name"], "description": s["lede"],
         "provider": {"@type": "Organization", "name": C.SITE["name"], "url": C.SITE["domain"] + "/"},
         "serviceType": s["en"], "url": C.SITE["domain"] + f'/servicios/{s["slug"]}/'},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in s["faqs"]]},
    ]
    write(f'servicios/{s["slug"]}/index.html', s["name"], s["lede"], body, active="servicios", crumbs=crumbs, ld=ld)


def build_industries_index():
    r = "../"
    crumbs = [("Industrias", "industrias/")]
    cards = "".join(f'''<a class="icard icard--lg rv" href="{r}industrias/{i["slug"]}/">{icon(i["icon"])}<h3>{e(i["name"])}</h3><p class="icard__tag">{e(i["tagline"])}</p><p>{e(i["lede"])}</p><span class="scard__more">Ver industria</span></a>''' for i in C.INDUSTRIES)
    body = phero(r, crumbs, "Industrias", "Sectores donde la tecnología es el negocio.",
                 "Llevamos las mismas capacidades a contextos con exigencias distintas: regulación, picos de demanda, información sensible. Conocer el sector cambia qué se prioriza y cómo se ejecuta.") + f'''
<section class="section section--paper">
  <div class="container"><div class="icards" data-stagger>{cards}</div></div>
</section>''' + cta_band(r)
    write("industrias/index.html", "Industrias", "Consultoría en TI para servicios financieros, retail y consumo, y salud y seguros.",
          body, active="industrias", crumbs=crumbs)


def build_industry(i):
    r = "../../"
    crumbs = [("Industrias", "industrias/"), (i["name"], f'industrias/{i["slug"]}/')]
    ctx = "".join(f'<p class="lede">{e(p)}</p>' for p in i["context"])
    ch = "".join(f'<li class="rv"><h3>{e(t)}</h3><p>{e(d)}</p></li>' for t, d in i["challenges"])
    hp = "".join(f'''<a class="helprow rv" href="{r}servicios/{sl}/"><span class="helprow__svc">{icon(SVC[sl]["icon"])}{e(SVC[sl]["name"])}</span><span class="helprow__txt">{e(t)}</span><span class="helprow__go" aria-hidden="true">{icon("arrow-right")}</span></a>''' for sl, t in i["help"])
    c = CASE[i["case"]]
    body = phero(r, crumbs, "Industrias", i["name"], i["lede"],
                 f'<div class="phero__actions rv"><a href="{r}contacto/?interes={i["slug"]}" class="btn btn--gold btn--lg">Conversar sobre su sector</a></div>') + f'''
<section class="section section--paper">
  <div class="container split split--even">
    <div class="rv"><p class="label label--dark">Contexto</p><h2 class="display">{e(i["tagline"])}</h2></div>
    <div class="rv">{ctx}</div>
  </div>
</section>
<section class="section section--light">
  <div class="container">
    {head("Retos del sector", "Lo que vemos en las organizaciones.")}
    <ul class="problems problems--4">{ch}</ul>
  </div>
</section>
<section class="framework">
  <div class="container">
    {head("Cómo ayudamos", "Capacidades aplicadas al sector.", dark=True)}
    <div class="helprows">{hp}</div>
  </div>
</section>
<section class="section section--paper">
  <div class="container">
    {head("Caso representativo", "Impacto en el sector.")}
    <a class="feature-case rv" href="{r}casos/{c["slug"]}/">
      <p class="case__meta">Caso {c["n"]} · {e(i["name"])}</p>
      <h3>{e(c["title"])}</h3>
      <p>{e(c["summary"])}</p>
      <span class="scard__more">Leer el caso completo</span>
    </a>
  </div>
</section>''' + cta_band(r)
    write(f'industrias/{i["slug"]}/index.html', i["name"], i["lede"], body, active="industrias", crumbs=crumbs)


def build_cases_index():
    r = "../"
    crumbs = [("Casos", "casos/")]
    cards = "".join(f'''<a class="case rv" href="{r}casos/{c["slug"]}/">
        <p class="case__meta">Caso {c["n"]} · {e(IND[c["industry"]]["name"])}</p>
        <h3 class="case__result">{e(c["title"])}</h3>
        <p class="case__sum">{e(c["summary"])}</p>
        <ul class="case__tags">{"".join(f"<li>{e(SVC[x]['name'])}</li>" for x in c["services"])}</ul>
        <span class="scard__more">Leer el caso</span>
      </a>''' for c in C.CASES)
    body = phero(r, crumbs, "Credentials & proof points", "Casos representativos e impacto.",
                 "Iniciativas en las que Oakmont respondió de la estrategia a la operación. Por confidencialidad, no publicamos el nombre de nuestros clientes; con gusto ampliamos el detalle en una conversación.") + f'''
<section class="section section--paper">
  <div class="container">
    <div class="cases" data-stagger>{cards}</div>
    <div class="partners-row rv"><span>Alianzas</span><ul class="partners"><li>AWS</li><li>Microsoft Azure</li><li>Google Cloud</li></ul></div>
  </div>
</section>''' + cta_band(r)
    write("casos/index.html", "Casos", "Casos representativos de modernización, operación cloud-native y plataformas de datos con IA aplicada.",
          body, active="casos", crumbs=crumbs)


def build_case(c):
    r = "../../"
    ind = IND[c["industry"]]
    crumbs = [("Casos", "casos/"), (f'Caso {c["n"]}', f'casos/{c["slug"]}/')]
    ch = "".join(f"<li>{e(x)}</li>" for x in c["challenge"])
    ap = "".join(f'<li class="rv"><span class="horizons__n">{["01","02","03"][k]}</span><div><h3>{e(t)}</h3><p>{e(d)}</p></div></li>' for k, (t, d) in enumerate(c["approach"]))
    sol = "".join(f'<li>{icon("check")}<span>{e(x)}</span></li>' for x in c["solution"])
    res = "".join(f'<li class="rv"><p>{e(x)}</p></li>' for x in c["results"])
    svcs = "".join(svc_card(r, SVC[x]) for x in c["services"][:3])
    others = [x for x in C.CASES if x["slug"] != c["slug"]]
    oth = "".join(f'<a class="case rv" href="{r}casos/{o["slug"]}/"><p class="case__meta">Caso {o["n"]} · {e(IND[o["industry"]]["name"])}</p><h3 class="case__result">{e(o["title"])}</h3><span class="scard__more">Leer el caso</span></a>' for o in others)
    body = phero(r, crumbs, f'Caso {c["n"]} · {ind["name"]}', c["title"], c["summary"]) + f'''
<section class="section section--paper">
  <div class="container with-aside">
    <div class="prose rv">
      <h2>Contexto</h2>
      <p>{e(c["context"])}</p>
      <h2>El reto</h2>
      <ul class="bullets">{ch}</ul>
    </div>
    <aside class="aside rv" aria-label="Ficha del caso">
      <p class="aside__h">Industria</p>
      <ul><li><a href="{r}industrias/{ind["slug"]}/">{e(ind["name"])}</a></li></ul>
      <p class="aside__h">Capacidades</p>
      <ul>{"".join(f'<li><a href="{r}servicios/{x}/">{e(SVC[x]["name"])}</a></li>' for x in c["services"])}</ul>
      <p class="aside__note">Por confidencialidad, el nombre del cliente no se publica.</p>
    </aside>
  </div>
</section>
<section class="framework">
  <div class="container">
    {head("Enfoque", "Cómo lo abordamos: Define, Evolve, Deliver.", dark=True)}
    <ol class="horizons horizons--wide" data-stagger>{ap}</ol>
  </div>
</section>
<section class="section section--light">
  <div class="container split split--even">
    <div class="rv"><p class="label label--dark">Solución</p><h2 class="display">Qué construimos.</h2></div>
    <ul class="checklist rv">{sol}</ul>
  </div>
</section>
<section class="section section--ivory">
  <div class="container">
    {head("Resultados", "Qué cambió.")}
    <ul class="results" data-stagger>{res}</ul>
  </div>
</section>
<section class="section section--paper">
  <div class="container">
    {head("Capacidades aplicadas", "Servicios que intervinieron.")}
    <div class="scards scards--3" data-stagger>{svcs}</div>
  </div>
</section>
<section class="section section--light">
  <div class="container">
    {head("Más casos", "Otros resultados.")}
    <div class="cases cases--2" data-stagger>{oth}</div>
  </div>
</section>''' + cta_band(r, title="¿Un reto parecido en su organización?")
    write(f'casos/{c["slug"]}/index.html', f'Caso {c["n"]}: {ind["name"]}', c["summary"], body, active="casos", crumbs=crumbs)


def build_approach():
    r = "../"
    crumbs = [("Enfoque", "enfoque/")]
    hz = "".join(f'''<li class="rv"><span class="horizons__n">{n}</span><div><h3>{t}</h3><p class="horizons__sub">{e(sub)}</p><p>{e(d)}</p><ul class="mini">{"".join(f"<li>{e(x)}</li>" for x in items)}</ul></div></li>''' for n, t, sub, d, items in C.HORIZONS)
    layer = "".join(f'<li class="rv"><h3>{e(t)}</h3><p>{e(d)}</p></li>' for t, d in C.LAYER)
    ph = "".join(f'<li><span class="phases__dot" aria-hidden="true"></span><span class="phases__n">{n}</span><h3>{t}</h3><p class="phases__lead">{e(a)}</p><p>{e(b)}</p></li>' for n, t, a, b in C.PHASES)
    gov = "".join(f'<li class="rv"><h3>{e(t)}</h3><p>{e(d)}</p></li>' for t, d in C.GOVERNANCE)
    ct = "".join(f'<tr><th scope="row">{e(t)}</th><td>{e(d)}</td><td>{e(w)}</td></tr>' for t, d, w in C.CONTRACTS)
    ms = "".join(f'<div class="figure"><strong class="figure__word">{e(t)}</strong><span>{e(d)}</span></div>' for t, d in C.MEASURES)
    body = phero(r, crumbs, "Enfoque", "Tres horizontes, un solo gobierno.",
                 "Define, Evolve y Deliver no son tres proveedores ni tres contratos: son tres horizontes de una misma iniciativa, con un solo responsable y un mismo tablero de indicadores.") + f'''
<section class="framework">
  <div class="container">
    <div class="framework__grid">
      {orbit_svg()}
      <ol class="horizons" data-stagger>{hz}</ol>
    </div>
  </div>
</section>
<section class="section section--light">
  <div class="container">
    {head("Capa transversal", "Lo que se mantiene de extremo a extremo.")}
    <ul class="outcomes outcomes--4" data-stagger>{layer}</ul>
  </div>
</section>
<section class="journey">
  <div class="container">
    {head("Modelo de engagement", "Cuatro fases, un solo responsable.", dark=True)}
    <ol class="phases phases--detail rv">{ph}</ol>
  </div>
</section>
<section class="section section--paper">
  <div class="container">
    {head("Delivery governance", "Cómo se gobierna cada iniciativa.")}
    <ul class="outcomes outcomes--4" data-stagger>{gov}</ul>
  </div>
</section>
<section class="section section--ivory">
  <div class="container">
    {head("Modelos contractuales", "La forma de contratar se adapta al reto.")}
    <div class="table-wrap rv">
      <table class="table">
        <thead><tr><th scope="col">Modelo</th><th scope="col">Qué es</th><th scope="col">Cuándo conviene</th></tr></thead>
        <tbody>{ct}</tbody>
      </table>
    </div>
  </div>
</section>
<section class="figures">
  <div class="container">
    {head("Cómo medimos el éxito", "Tres métricas acordadas antes de empezar.")}
    <div class="figures__grid figures__grid--3 rv">{ms}</div>
  </div>
</section>''' + cta_band(r)
    write("enfoque/index.html", "Enfoque", "Framework Define, Evolve, Deliver; modelo de engagement; gobierno de entrega y modelos contractuales de Oakmont Services.",
          body, active="enfoque", crumbs=crumbs)


def build_about():
    r = "../"
    crumbs = [("Nosotros", "nosotros/")]
    reasons = "".join(f'<li><span>{n}</span><h3>{e(t)}</h3><p>{e(d)}</p></li>' for n, t, d in C.REASONS)
    body = phero(r, crumbs, "Nosotros", "Un socio estratégico, no un proveedor transaccional.",
                 "Oakmont Services es una consultora especializada en tecnologías de la información que acompaña a la dirección ejecutiva en la definición, evolución e implementación de soluciones tecnológicas.") + f'''
<section class="section section--paper">
  <div class="container split">
    <div class="rv">
      <p class="label label--dark">Quiénes somos</p>
      <h2 class="display">Advisory y delivery bajo un mismo techo.</h2>
      <p class="lede">Integramos estrategia, arquitectura e ingeniería en un solo equipo. La estrategia que diseñamos es la misma que ejecutamos y de la que respondemos.</p>
      <p class="lede">Trabajamos con la dirección ejecutiva y con los equipos de tecnología, en el lenguaje de cada uno: valor, costo y riesgo para la dirección; arquitectura, calidad y operación para los equipos.</p>
    </div>
    <figure class="split__media rv">
      <img src="{r}images/reception.jpg" alt="Recepción de las oficinas de Oakmont Services" width="387" height="523" loading="lazy">
      <figcaption>Discreción, excelencia y alto nivel de servicio.</figcaption>
    </figure>
  </div>
</section>
<section class="manifesto">
  <div class="container">
    <p class="label rv">Propósito</p>
    <p class="manifesto__text rv">La distancia entre la ambición tecnológica y su ejecución es donde se gana o se pierde la ventaja. <em>Oakmont existe para cerrarla.</em></p>
  </div>
</section>
<section class="why">
  <div class="why__bg" aria-hidden="true"><img src="{r}images/globe.jpg" alt="" width="532" height="474" loading="lazy"></div>
  <div class="container">
    {head("Principios", "Cinco compromisos que guían cada iniciativa.", dark=True)}
    <ol class="reasons reasons--long rv">{reasons}</ol>
  </div>
</section>
<section class="section section--light">
  <div class="container">
    {head("Talento", "Seniority validada, no declarada.")}
    <ul class="outcomes" data-stagger>
      <li class="rv"><h3>Evaluación práctica</h3><p>Cada profesional resuelve problemas reales del rol antes de incorporarse a un proyecto.</p></li>
      <li class="rv"><h3>Ajuste cultural</h3><p>Entrevista con un líder senior para validar comunicación, criterio y forma de trabajo.</p></li>
      <li class="rv"><h3>Seguimiento continuo</h3><p>Revisiones periódicas de desempeño y reemplazo garantizado cuando un perfil no cumple.</p></li>
    </ul>
  </div>
</section>
<section class="section section--paper">
  <div class="container split split--even">
    <div class="rv"><p class="label label--dark">Neutralidad tecnológica</p><h2 class="display">Independencia al servicio del negocio.</h2></div>
    <div class="rv">
      <p class="lede">Mantenemos alianzas con AWS, Microsoft Azure y Google Cloud, y recomendamos en cada caso la tecnología que mejor sirve al negocio. Nuestras recomendaciones no dependen de acuerdos comerciales con fabricantes.</p>
      <ul class="partners partners--lg"><li>AWS</li><li>Microsoft Azure</li><li>Google Cloud</li></ul>
    </div>
  </div>
</section>''' + cta_band(r)
    write("nosotros/index.html", "Nosotros", "Quiénes somos, propósito, principios y modelo de talento de Oakmont Services.",
          body, active="nosotros", crumbs=crumbs)


def build_diagnostic():
    r = "../"
    crumbs = [("Diagnóstico estratégico", "diagnostico/")]
    D = C.DIAGNOSTIC
    weeks = "".join(f'''<div class="week rv"><p class="week__h">{e(w)}</p><h3>{e(t)}</h3><ul>{"".join(f"<li>{e(x)}</li>" for x in items)}</ul></div>''' for w, t, items in D["weeks"])
    dl = "".join(f'<li class="rv"><h3>{e(t)}</h3><p>{e(d)}</p></li>' for t, d in D["deliverables"])
    needs = "".join(f'<li>{icon("check")}<span>{e(x)}</span></li>' for x in D["needs"])
    body = phero(r, crumbs, "Diagnóstico estratégico", "Dos semanas para saber dónde está y qué hacer primero.",
                 "Un diagnóstico acotado de su tecnología con hallazgos accionables y prioridades claras. Sin compromiso de contratación posterior.",
                 f'<div class="phero__actions rv"><a href="{r}contacto/?interes=diagnostico" class="btn btn--gold btn--lg">Solicitar diagnóstico</a></div>') + f'''
<section class="section section--paper">
  <div class="container">
    {head("Agenda", "Cómo se usan las dos semanas.")}
    <div class="weeks" data-stagger>{weeks}</div>
  </div>
</section>
<section class="section section--ivory">
  <div class="container">
    {head("Entregables", "Lo que recibe al terminar.")}
    <ul class="outcomes outcomes--4" data-stagger>{dl}</ul>
  </div>
</section>
<section class="section section--light">
  <div class="container split split--even">
    <div class="rv"><p class="label label--dark">Qué necesitamos</p><h2 class="display">Su participación, acotada.</h2></div>
    <ul class="checklist rv">{needs}</ul>
  </div>
</section>
<section class="section section--paper">
  <div class="container split split--even">
    <div class="rv"><p class="label label--dark">Para quién es</p><h2 class="display">Direcciones que deben decidir con información.</h2></div>
    <div class="rv">
      <p class="lede">Direcciones generales, de finanzas, de operaciones y de tecnología que enfrentan una decisión relevante: modernizar sistemas centrales, migrar a la nube, ordenar el portafolio de proveedores o incorporar IA.</p>
      <p class="lede">Al terminar, usted decide si continúa con Oakmont, con otro proveedor o con su propio equipo. Los entregables son suyos.</p>
    </div>
  </div>
</section>''' + cta_band(r, title="Agende la sesión de arranque.", text="Respondemos en un máximo de dos días hábiles para acordar fechas y participantes.")
    write("diagnostico/index.html", "Diagnóstico estratégico de dos semanas", "Diagnóstico tecnológico de dos semanas con hallazgos accionables, riesgos priorizados e iniciativas por horizonte.",
          body, crumbs=crumbs)


def build_contact():
    r = "../"
    crumbs = [("Contacto", "contacto/")]
    opts = '<option value="">Seleccione una opción</option><option value="diagnostico">Diagnóstico estratégico de dos semanas</option>'
    opts += "".join(f'<option value="{s["slug"]}">{e(s["name"])}</option>' for s in C.SERVICES)
    opts += "".join(f'<option value="{i["slug"]}">Industria: {e(i["name"])}</option>' for i in C.INDUSTRIES)
    opts += '<option value="otro">Otro tema</option>'
    body = phero(r, crumbs, "Contacto", "Conversemos.",
                 "Cuéntenos su contexto y el reto que enfrenta. Un socio de Oakmont le responderá en un máximo de dos días hábiles.") + f'''
<section class="section section--paper">
  <div class="container with-aside">
    <form class="form rv" id="contact-form" action="/api/contacto" method="post" novalidate>
      <p class="form__ok" role="status" hidden>Gracias. Recibimos su mensaje y un socio de Oakmont le responderá en un máximo de dos días hábiles.</p>
      <div class="form__row">
        <label class="field"><span>Nombre completo *</span><input name="nombre" autocomplete="name" maxlength="120" required></label>
        <label class="field"><span>Correo corporativo *</span><input name="correo" type="email" autocomplete="email" maxlength="160" required></label>
      </div>
      <div class="form__row">
        <label class="field"><span>Empresa *</span><input name="empresa" autocomplete="organization" maxlength="160" required></label>
        <label class="field"><span>Cargo</span><input name="cargo" autocomplete="organization-title" maxlength="120"></label>
      </div>
      <div class="form__row">
        <label class="field"><span>Teléfono</span><input name="telefono" type="tel" autocomplete="tel" maxlength="40"></label>
        <label class="field"><span>Tema de interés *</span><select name="interes" required>{opts}</select></label>
      </div>
      <label class="field"><span>¿Qué reto quiere resolver? *</span><textarea name="mensaje" rows="6" maxlength="5000" required></textarea></label>
      <div class="hp" aria-hidden="true"><label>No llene este campo <input name="sitio_web" tabindex="-1" autocomplete="off"></label></div>
      <input type="hidden" name="ts" value="">
      <input type="hidden" name="interes_label" value="">
      <input type="hidden" name="pagina_origen" value="">
      <label class="check"><input type="checkbox" name="privacidad" required><span>He leído y acepto el <a href="{r}aviso-de-privacidad/">aviso de privacidad</a>. *</span></label>
      <p class="form__error" role="alert" hidden>Revise los campos marcados con *.</p>
      <div class="form__actions">
        <button class="btn btn--dark btn--lg" type="submit">Enviar mensaje</button>
        <p class="form__note">Sus datos se usan solo para responder a su solicitud.</p>
      </div>
    </form>
    <aside class="aside rv" aria-label="Otras formas de contacto">
      <p class="aside__h">Correo</p>
      <p><a href="mailto:{C.SITE["email"]}">{C.SITE["email"]}</a></p>
      <p class="aside__h">LinkedIn</p>
      <p><a href="{C.SITE["linkedin"]}" rel="noopener" target="_blank">Oakmont Services</a></p>
      <p class="aside__h">Qué pasa después</p>
      <ol class="steps-mini">
        <li>Revisamos su mensaje y asignamos a un socio con experiencia en su tema.</li>
        <li>Agendamos una conversación de 45 minutos para entender su contexto.</li>
        <li>Le proponemos el siguiente paso: diagnóstico, propuesta o referencia.</li>
      </ol>
    </aside>
  </div>
</section>'''
    write("contacto/index.html", "Contacto", "Contacte a Oakmont Services para conversar sobre estrategia, arquitectura, ingeniería, nube, datos e IA.",
          body, crumbs=crumbs)


def build_privacy():
    r = "../"
    crumbs = [("Aviso de privacidad", "aviso-de-privacidad/")]
    S = C.SITE
    body = phero(r, crumbs, "Legal", "Aviso de privacidad", "Cómo tratamos los datos personales que usted nos comparte a través de este sitio.") + f'''
<section class="section section--paper">
  <div class="container">
    <div class="prose prose--legal">
      <p><em>Última actualización: noviembre de 2026.</em></p>
      <h2>Responsable del tratamiento</h2>
      <p>{e(S["legal_name"])} (en adelante, «Oakmont Services»), con domicilio en {e(S["legal_address"])}, es responsable del tratamiento de sus datos personales conforme a la Ley Federal de Protección de Datos Personales en Posesión de los Particulares y su normativa aplicable.</p>
      <h2>Datos que recabamos</h2>
      <p>A través del formulario de contacto y del correo electrónico recabamos: nombre, correo electrónico corporativo, empresa, cargo, teléfono y la información que usted decida incluir en su mensaje. No solicitamos datos personales sensibles.</p>
      <h2>Finalidades</h2>
      <p>Finalidades primarias: atender su solicitud de contacto, agendar reuniones, elaborar propuestas de servicios y dar seguimiento a la relación comercial.</p>
      <p>Finalidades secundarias: enviarle información sobre servicios, publicaciones o eventos de Oakmont Services. Si no desea que sus datos se usen para estas finalidades, puede indicarlo en cualquier momento escribiendo a <a href="mailto:{S["email"]}">{S["email"]}</a>.</p>
      <h2>Transferencias</h2>
      <p>No transferimos sus datos personales a terceros sin su consentimiento, salvo en los casos previstos por la ley. Los datos enviados mediante el formulario se almacenan en la infraestructura de Vercel Inc., proveedor de alojamiento del sitio, que los trata por cuenta de Oakmont Services. También podemos apoyarnos en otros proveedores de servicios tecnológicos, como correo electrónico, bajo obligaciones de confidencialidad.</p>
      <h2>Derechos ARCO</h2>
      <p>Usted puede acceder, rectificar, cancelar u oponerse al tratamiento de sus datos personales, así como revocar su consentimiento, enviando una solicitud a <a href="mailto:{S["email"]}">{S["email"]}</a> con su nombre, un medio para comunicarle la respuesta, la descripción clara de los datos y el derecho que desea ejercer, y una copia de su identificación. Responderemos en los plazos que establece la ley.</p>
      <h2>Cookies y tecnologías similares</h2>
      <p>Este sitio no utiliza cookies propias de rastreo ni publicidad. Las fuentes tipográficas e íconos se cargan desde proveedores externos (Google Fonts y unpkg), que pueden registrar datos técnicos de la conexión, como la dirección IP, conforme a sus propias políticas.</p>
      <h2>Cambios a este aviso</h2>
      <p>Cualquier modificación a este aviso de privacidad se publicará en esta misma página.</p>
    </div>
  </div>
</section>'''
    write("aviso-de-privacidad/index.html", "Aviso de privacidad", "Aviso de privacidad de Oakmont Services.", body, crumbs=crumbs)


def build_404():
    r = "/"
    body = f'''
<section class="phero phero--404">
  <div class="container">
    <p class="label">Error 404</p>
    <h1 class="phero__title">Esta página no existe.</h1>
    <p class="phero__lede">Es posible que el enlace haya cambiado. Estas secciones pueden ayudarle:</p>
    <div class="phero__actions">
      <a href="{r}" class="btn btn--gold btn--lg">Ir al inicio</a>
      <a href="{r}servicios/" class="link-arrow">Servicios</a>
      <a href="{r}contacto/" class="link-arrow">Contacto</a>
    </div>
  </div>
</section>'''
    write("404.html", "Página no encontrada", "La página solicitada no existe.", body, r=r)


def build_meta():
    urls = "".join(f"  <url><loc>{C.SITE['domain']}/{p}</loc></url>\n" for p in PAGES)
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\nDisallow: /admin/\nDisallow: /api/\n\nSitemap: {C.SITE['domain']}/sitemap.xml\n")


if __name__ == "__main__":
    build_home()
    build_services_index()
    for s in C.SERVICES:
        build_service(s)
    build_industries_index()
    for i in C.INDUSTRIES:
        build_industry(i)
    build_cases_index()
    for c in C.CASES:
        build_case(c)
    build_approach()
    build_about()
    build_diagnostic()
    build_contact()
    build_privacy()
    build_404()
    build_meta()
    print(f"Generated {len(PAGES) + 1} pages + sitemap.xml + robots.txt")

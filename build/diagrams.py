# -*- coding: utf-8 -*-
"""
Allegorical diagrams for the page headers.

Each diagram explains its page's idea while it draws itself, once, when it
enters the viewport. Shared vocabulary (styled in css/styles.css, .allegory):

  draw   stroke drawn from start to end      (needs pathLength="1")
  fade   fades in                            (labels, dots, dashed guides)
  g/g2/g3  gold stroke at 100 / 60 / 35 % ; w = faint ivory stroke
  dash   dashed guide line ; fill = solid gold ; tint = soft gold area
  text classes: dim, gold, big, s (anchor start), e (anchor end)

--t is the start delay in seconds and --dur the drawing time, so every
diagram unfolds in the order its story is told.
"""
import math


def _st(t, dur=None):
    return f' style="--t:{t}s' + (f';--dur:{dur}s' if dur else '') + '"'


def path(d, cls="g", t=0.0, dur=1.0):
    return f'<path class="draw {cls}" d="{d}" pathLength="1"{_st(t, dur)}/>'


def circle(cx, cy, r, cls="g", t=0.0, dur=1.0, draw=True):
    kind = "draw" if draw else "fade"
    pl = ' pathLength="1"' if draw else ""
    return f'<circle class="{kind} {cls}" cx="{cx}" cy="{cy}" r="{r}"{pl}{_st(t, dur if draw else None)}/>'


def dot(cx, cy, r=5, t=0.0, cls="fill"):
    return f'<circle class="fade {cls}" cx="{cx}" cy="{cy}" r="{r}"{_st(t)}/>'


def rect(x, y, w, h, cls="fill", t=0.0, rx=0):
    return f'<rect class="fade {cls}" x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}"{_st(t)}/>'


def guide(d, t=0.0, cls="w dash"):
    return f'<path class="fade {cls}" d="{d}"{_st(t)}/>'


def label(x, y, text, t=0.0, cls=""):
    return f'<text class="{("fade " + cls).strip()}" x="{x}" y="{y}"{_st(t)}>{text}</text>'


def hexagon(cx, cy, r):
    pts = [(cx + r * math.sin(math.radians(a)), cy - r * math.cos(math.radians(a))) for a in range(0, 360, 60)]
    return "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts) + " Z"


def toward(x1, y1, x2, y2, stop):
    """Point on the segment (x1,y1)->(x2,y2) that is `stop` px short of (x2,y2)."""
    dx, dy = x2 - x1, y2 - y1
    d = math.hypot(dx, dy)
    return x2 - dx / d * stop, y2 - dy / d * stop


# --------------------------------------------------------------------------
# Diagrams: slug -> (accessible description, svg body)
# --------------------------------------------------------------------------
def _horizons():
    return ("Tres horizontes concéntricos — Define, Evolve y Deliver — dentro de una misma capa de gobierno",
            circle(200, 200, 58, "g", .2) + circle(200, 200, 104, "g2", .6) + circle(200, 200, 150, "g3", 1.0)
            + circle(200, 200, 190, "w dash", 1.4, draw=False)
            + label(200, 204, "DEFINE", .2) + label(200, 116, "EVOLVE", .6) + label(200, 70, "DELIVER", 1.0)
            + label(200, 24, "GOBIERNO", 1.4, "dim"))


def _fabrica():
    cx, cy, r = 160, 200, 80
    body = guide("M12 60 H388 V340 H12 Z", 2.2) + label(200, 48, "GOBIERNO DE ENTREGA", 2.2, "dim")
    body += circle(cx, cy, r, "g", .2, 1.4)
    stops = [(cx, cy - r, "CONSTRUIR", cx, cy - r - 16, ""), (cx - 69, cy + 40, "PROBAR", cx - 80, cy + 64, "e"),
             (cx + 69, cy + 40, "LIBERAR", cx + 80, cy + 64, "s")]
    for i, (x, y, text, lx, ly, anchor) in enumerate(stops):
        body += dot(x, y, 5, .5 + i * .35) + label(lx, ly, text, .5 + i * .35, anchor)
    body += label(cx, cy + 4, "CÉLULA", .3, "gold")
    body += path(f"M{cx+r} {cy} H372", "g2", 1.4, .8)
    for i, x in enumerate((276, 316, 356)):
        body += rect(x - 7, cy - 7, 14, 14, "fill", 1.8 + i * .25)
    body += label(316, cy - 22, "PRODUCCIÓN", 2.4)
    return ("Una célula de ingeniería trabaja en ciclo — construir, probar, liberar — y entrega incrementos a producción dentro de un gobierno de entrega", body)


def _strategy():
    body = ""
    for x in range(60, 360, 40):
        for y in range(80, 340, 40):
            body += f'<circle class="fade grid-dot" cx="{x}" cy="{y}" r="1.2"{_st(.1)}/>'
    body += path("M50 320 H130 V250 H210 V180 H290 V110 H350", "g", .3, 1.8)
    for i, (x, y) in enumerate(((130, 250), (210, 180), (290, 110))):
        body += dot(x, y, 5, .7 + i * .45) + label(x + 22, y - 10, f"0{i+1}", .7 + i * .45, "gold")
    body += dot(50, 320, 6, .2, "fill") + label(50, 350, "ESTADO ACTUAL", .2, "s")
    body += circle(350, 110, 12, "g", 2.0, .6) + dot(350, 110, 5, 2.1) + label(350, 80, "ESTADO OBJETIVO", 2.2, "e")
    return ("Una hoja de ruta en escalones que lleva del estado actual al estado objetivo, con tres hitos priorizados", body)


def _staff():
    team = [(150, 175), (200, 140), (250, 175), (230, 235), (170, 235)]
    body = ""
    for i, (a, b) in enumerate(zip(team, team[1:] + team[:1])):
        body += path(f"M{a[0]} {a[1]} L{b[0]} {b[1]}", "w", .2 + i * .1, .5)
    for (x, y) in team:
        body += circle(x, y, 13, "w-solid", .1, .6)
    talent = [((320, 120), team[2]), ((300, 300), team[3]), ((85, 290), team[4])]
    for i, ((x, y), (tx, ty)) in enumerate(talent):
        sx, sy = toward(x, y, tx, ty, 13)
        body += path(f"M{x} {y} L{sx:.1f} {sy:.1f}", "g2", 1.0 + i * .3, .6)
        body += dot(x, y, 11, .9 + i * .3)
    body += label(200, 272, "SU EQUIPO", .5)
    body += label(320, 96, "TALENTO VALIDADO", 1.2, "gold")
    body += circle(200, 200, 172, "w dash", 2.0, draw=False) + label(200, 22, "SEGUIMIENTO CONTINUO", 2.0, "dim")
    return ("Profesionales validados se integran y se conectan con el equipo del cliente, con seguimiento continuo", body)


def _cloud():
    hub = (80, 200)
    dests = [(250, 80, "AWS"), (250, 160, "AZURE"), (250, 240, "GOOGLE CLOUD"), (250, 320, "PROPIO")]
    body = circle(*hub, 30, "g", .1, .7) + label(80, 207, "7R", .3, "big gold")
    body += label(80, 252, "PORTAFOLIO", .3)
    for i, (x, y, text) in enumerate(dests):
        body += path(f"M110 200 C 190 200, 200 {y}, {x - 8} {y}", "g2" if text != "PROPIO" else "w", .6 + i * .25, .9)
        body += dot(x, y, 7, 1.3 + i * .25) + label(x + 16, y + 4, text, 1.3 + i * .25, "s")
    return ("Cada aplicación del portafolio se evalúa bajo el marco 7R y va a la nube que le conviene o se queda en infraestructura propia", body)


def _data():
    pts = [(48, 96), (92, 120), (60, 150), (110, 168), (44, 200), (86, 212), (122, 236), (58, 256),
           (100, 282), (48, 306), (128, 300), (76, 334)]
    body = ""
    for i, (x, y) in enumerate(pts):
        body += dot(x, y, 3.5, .05 + i * .04, "fill-dim")
        ex, ey = toward(x, y, 240, 200, 24)
        body += path(f"M{x} {y} L{ex:.1f} {ey:.1f}", "g3", .6 + i * .03, .7)
    body += circle(240, 200, 24, "g", 1.3, .6) + label(240, 245, "MODELO", 1.3)
    body += path("M264 200 H342", "g", 1.8, .5) + dot(350, 200, 8, 2.2) + label(350, 236, "DECISIÓN", 2.2, "gold")
    body += label(86, 365, "DATOS", .3, "dim")
    return ("Datos dispersos convergen en un modelo que produce una decisión", body)


def _cyber():
    body = ""
    rings = [(70, "APLICACIONES", .2), (110, "RED Y NUBE", .7), (150, "IDENTIDAD", 1.2)]
    for r, text, t in rings:
        body += path(hexagon(200, 205, r), "g" if r == 70 else ("g2" if r == 110 else "g3"), t, .9)
        body += label(200, 205 - r + 22, text, t + .3)
    body += dot(200, 205, 6, .1) + label(200, 232, "DATOS", .1, "gold")
    return ("La seguridad se diseña por capas alrededor de los datos: aplicaciones, red y nube, e identidad", body)


def _ops():
    body = rect(40, 110, 320, 40, "tint", .2) + guide("M40 150 H360", .2, "g3 dash")
    body += label(40, 100, "OBJETIVO DE SERVICIO", .3, "s dim")
    body += path("M40 320 H360", "w", .1, .6)
    body += path("M40 232 L72 186 L100 218 L130 160 L160 196 L190 142 L220 138 L260 132 L300 130 L340 128 L360 127", "g", .5, 1.8)
    body += label(360, 116, "DISPONIBILIDAD", 2.2, "e gold")
    body += path("M40 176 C 140 182, 220 250, 360 270", "w-solid", .9, 1.6) + label(360, 292, "COSTO", 2.4, "e")
    for i, (x, text) in enumerate(((90, "ESTABILIZAR"), (200, "AUTOMATIZAR"), (310, "OPTIMIZAR"))):
        body += label(x, 346, text, .8 + i * .5, "dim")
    return ("La disponibilidad se estabiliza dentro del objetivo de servicio mientras el costo de la plataforma baja", body)


def _quality():
    body = path("M40 200 H352", "g", .2, 1.8)
    gates = [(110, "UNITARIAS", 276), (170, "API", 134), (230, "CARGA", 276), (290, "SEGURIDAD", 134)]
    for i, (x, text, ly) in enumerate(gates):
        body += path(f"M{x} 150 V250", "g2", .4 + i * .25, .5) + label(x, ly, text, .4 + i * .25)
    for i, (x, y) in enumerate(((98, 176), (158, 226), (218, 172), (278, 228))):
        body += path(f"M{x-5} {y-5} L{x+5} {y+5} M{x+5} {y-5} L{x-5} {y+5}", "w-solid", 1.3 + i * .2, .3)
    body += label(40, 230, "CÓDIGO", .2, "s dim")
    body += dot(360, 200, 8, 2.0) + label(360, 236, "USUARIO", 2.0, "e gold")
    return ("El software atraviesa compuertas de prueba que detienen los defectos antes de llegar al usuario", body)


def _finance():
    body = rect(160, 160, 80, 80, "tint", .1) + path("M160 160 H240 V240 H160 Z", "g", .1, .9)
    body += label(200, 205, "NÚCLEO", .4, "gold")
    nodes = [((200, 60), "APP", (200, 40)), ((340, 200), "WEB", (340, 178)),
             ((200, 340), "PAGOS", (200, 372)), ((60, 200), "SUCURSAL", (60, 178))]
    for i, ((x, y), text, (lx, ly)) in enumerate(nodes):
        sx = 200 if x == 200 else (240 if x > 200 else 160)
        sy = 200 if y == 200 else (240 if y > 200 else 160)
        body += path(f"M{sx} {sy} L{x} {y}", "g2", .7 + i * .25, .6)
        mx, my = (sx + x) / 2, (sy + y) / 2
        body += rect(mx - 5, my - 5, 10, 10, "fill", 1.1 + i * .25)
        body += circle(x, y, 10, "w-solid", 1.0 + i * .25, .5) + label(lx, ly, text, 1.0 + i * .25)
    body += label(214, 114, "API", 2.0, "s dim")
    return ("Un núcleo transaccional desacoplado expone APIs gobernadas a sus canales: app, web, pagos y sucursales", body)


def _retail():
    body = path("M40 320 H360", "w", .1, .6)
    body += path("M40 270 L80 262 L105 215 L130 122 L152 214 L190 256 L230 246 L252 176 L272 100 L292 196 L330 252 L360 256", "g", .3, 1.6)
    body += path("M40 236 H96 V96 H166 V226 H244 V76 H304 V226 H360", "w-solid", .9, 1.6)
    body += path("M40 44 H64", "g", .2, .3) + label(74, 48, "DEMANDA", .2, "s")
    body += path("M40 66 H64", "w-solid", .9, .3) + label(74, 70, "CAPACIDAD", .9, "s")
    body += label(131, 346, "TEMPORADA", 1.8, "dim") + label(272, 346, "CAMPAÑA", 2.0, "dim")
    return ("La capacidad de la plataforma se ajusta por encima de la demanda en temporadas y campañas", body)


def _health():
    srcs = [((70, 90), "PÓLIZAS", (70, 66)), ((330, 90), "SINIESTROS", (330, 66)),
            ((70, 310), "CLIENTES", (70, 346)), ((330, 310), "PROVEEDORES", (330, 346))]
    body = ""
    for i, ((x, y), text, (lx, ly)) in enumerate(srcs):
        body += dot(x, y, 7, .1 + i * .15, "fill-dim") + label(lx, ly, text, .1 + i * .15)
        ex, ey = toward(x, y, 200, 200, 46)
        body += path(f"M{x} {y} L{ex:.1f} {ey:.1f}", "g3", .6 + i * .15, .7)
    body += circle(200, 200, 44, "g", 1.3, .8) + rect(156, 156, 88, 88, "tint-round", 1.4, 44)
    body += label(200, 197, "FUENTE", 1.5, "gold") + label(200, 213, "ÚNICA", 1.5, "gold")
    body += circle(200, 200, 64, "w dash", 2.0, draw=False) + label(200, 120, "GOBIERNO Y PRIVACIDAD", 2.1, "dim")
    return ("Información de pólizas, siniestros, clientes y proveedores converge en una fuente única, gobernada y protegida", body)


def _system():
    """Home hero: strategy, architecture and execution orchestrated as one system."""
    body = guide("M20 208 H380", .1, "w dash") + guide("M200 20 V380", .1, "w dash")
    body += path("M200 150 L150 237 L250 237 Z", "w", .2, .8)
    parts = [((200, 150), "g", .4, (200, 72), (200, 40), (200, 28), "ESTRATEGIA"),
             ((150, 237), "g2", .9, (95, 292), (62, 326), (62, 346), "ARQUITECTURA"),
             ((250, 237), "g2", 1.4, (305, 292), (338, 326), (338, 346), "EJECUCIÓN")]
    for (cx, cy), cls, t, (ax, ay), (bx, by), (lx, ly), text in parts:
        body += circle(cx, cy, 78, cls, t, 1.2)
        body += path(f"M{ax} {ay} L{bx} {by}", "w-solid", t + .8, .4) + label(lx, ly, text, t + .9)
    body += circle(200, 208, 160, "g3", 2.0, 1.4)
    body += dot(200, 208, 7, 2.9) + circle(200, 208, 16, "g", 3.0, .6)
    body += label(200, 392, "UN SISTEMA ÚNICO", 3.1, "gold")
    return ("Estrategia, arquitectura y ejecución se superponen y quedan orquestadas en un sistema único; en su centro, la ventaja", body)


DIAGRAMS = {
    "sistema": _system,
    "horizontes": _horizons,
    "fabrica-de-software": _fabrica,
    "strategy-advisory": _strategy,
    "staff-augmentation": _staff,
    "cloud-multicloud": _cloud,
    "data-ai": _data,
    "cyber-trust": _cyber,
    "cloud-operations": _ops,
    "quality-engineering": _quality,
    "servicios-financieros": _finance,
    "retail-y-consumo": _retail,
    "salud-y-seguros": _health,
}


def svg(key):
    desc, body = DIAGRAMS[key]()
    return (f'<svg class="allegory__svg" viewBox="0 0 400 400" role="img" aria-label="{desc}">'
            f'{body}</svg>')

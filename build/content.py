# -*- coding: utf-8 -*-
"""
Oakmont Services — site content.

Single source of truth for every page. Edit text here and run:

    python3 build/build.py

Rules followed when writing this content:
- No client names, no invented metrics, no founding year, no headcount,
  no office addresses. Results are stated qualitatively.
- Every service page answers: when do I need it, what exactly do you do,
  how do you work, what do I receive, how can I contract it, what changes.
"""

SITE = {
    "name": "Oakmont Services",
    "tagline": "Architecting Technology Advantage",
    "domain": "https://oakmontservices.com",
    "email": "contacto@oakmontservices.com",
    "linkedin": "https://www.linkedin.com/company/oakmont-services",
    "description": "Consultoría en tecnologías de la información. Estrategia, arquitectura e ingeniería bajo un modelo de gobierno único, de la estrategia a la producción.",
    # Completar antes de publicar el aviso de privacidad:
    "legal_name": "[Razón social de Oakmont Services]",
    "legal_address": "[Domicilio fiscal completo]",
}

# --------------------------------------------------------------------------
# Services
# --------------------------------------------------------------------------
SERVICES = [
    {
        "slug": "fabrica-de-software",
        "name": "Fábrica de Software",
        "sub": "Ingeniería de software gestionada",
        "plane": "nucleo",
        "icon": "layers",
        "short": "Entrega gestionada por células, con procesos, niveles de servicio y gobierno de entrega.",
        "tagline": "Software de producción, entregado con la disciplina de una operación.",
        "lede": "Células de ingeniería gestionadas por Oakmont que diseñan, construyen y evolucionan sus productos digitales con procesos definidos, niveles de servicio acordados y un gobierno de entrega medible.",
        "problems": [
            ("Un backlog que crece más rápido que la capacidad", "Las iniciativas del negocio esperan trimestres por una capacidad de desarrollo que no llega."),
            ("Proveedores que entregan horas, no resultados", "Modelos por tiempo y materiales sin compromiso sobre calidad, plazos ni costo total."),
            ("Calidad impredecible en producción", "Defectos que aparecen en producción y retrabajo que consume el presupuesto destinado a evolucionar."),
        ],
        "offerings": [
            ("Desarrollo de productos digitales", "Aplicaciones web y móviles, portales y plataformas transaccionales, desde el descubrimiento hasta la operación."),
            ("Modernización de aplicaciones", "Rearquitectura de sistemas legados hacia servicios desacoplados, por etapas y sin detener la operación."),
            ("Integración y APIs", "Capas de integración, APIs gobernadas y orquestación entre sistemas centrales, SaaS y nube."),
            ("Mantenimiento evolutivo", "Evolución continua del portafolio de aplicaciones con niveles de servicio acordados."),
            ("Ingeniería de plataforma", "Pipelines de integración y despliegue continuos, entornos reproducibles y prácticas DevSecOps desde el primer sprint."),
        ],
        "approach": [
            ("Descubrimiento", "Alcance, arquitectura de solución y backlog priorizado por valor de negocio."),
            ("Conformación de células", "Equipos multidisciplinarios dimensionados al alcance: liderazgo técnico, ingeniería, calidad y DevOps."),
            ("Entrega iterativa", "Incrementos funcionales en ciclos cortos, con demostraciones y métricas de flujo visibles para el cliente."),
            ("Gobierno y niveles de servicio", "Comité de seguimiento con indicadores de calidad, productividad y cumplimiento de niveles de servicio."),
        ],
        "deliverables": [
            "Software en producción con documentación técnica y funcional",
            "Arquitectura de solución y registro de decisiones técnicas",
            "Pipelines de integración y despliegue continuos",
            "Suite de pruebas automatizadas",
            "Tablero de métricas de entrega y niveles de servicio",
            "Plan de transferencia de conocimiento",
        ],
        "models": ["Proyecto a precio cerrado", "Célula dedicada con capacidad mensual", "Servicio gestionado con niveles de servicio"],
        "outcomes": [
            ("Previsibilidad", "Alcance, plazo y costo gestionados por un solo responsable."),
            ("Velocidad sostenible", "Ciclos de entrega más cortos sin acumular deuda técnica."),
            ("Calidad desde el diseño", "Pruebas automatizadas y revisión de arquitectura en cada incremento."),
        ],
        "faqs": [
            ("¿Quién es dueño del código?", "El cliente. El código, la documentación y los artefactos se entregan en sus repositorios desde el primer día."),
            ("¿Pueden trabajar junto con nuestro equipo interno?", "Sí. Las células operan de forma autónoma o integradas con sus equipos, bajo un mismo gobierno de entrega."),
            ("¿Con qué tecnologías trabajan?", "Elegimos la tecnología según el contexto de cada cliente; no estamos atados a un fabricante. Construimos sobre AWS, Microsoft Azure y Google Cloud."),
        ],
        "related": ["quality-engineering", "cloud-operations", "strategy-advisory"],
    },
    {
        "slug": "strategy-advisory",
        "name": "Strategy & Advisory",
        "sub": "Estrategia tecnológica",
        "plane": "nucleo",
        "icon": "compass",
        "short": "Diagnóstico, arquitectura objetivo, roadmap multianual y caso de negocio.",
        "tagline": "Decisiones tecnológicas con caso de negocio, no por tendencia.",
        "lede": "Acompañamos a la dirección ejecutiva a definir qué construir, en qué orden y con qué retorno: diagnóstico, arquitectura objetivo, roadmap multianual y caso de negocio.",
        "problems": [
            ("Inversión sin dirección común", "Iniciativas tecnológicas aisladas que compiten por presupuesto sin una visión compartida."),
            ("Una arquitectura que nadie diseñó", "Un ecosistema que creció por acumulación y hoy limita la velocidad del negocio."),
            ("Decisiones difíciles de sustentar", "Comités que necesitan costos, beneficios y riesgos claros para aprobar una transformación."),
        ],
        "offerings": [
            ("Diagnóstico tecnológico", "Evaluación del estado actual de aplicaciones, infraestructura, datos, seguridad y organización de TI."),
            ("Arquitectura empresarial objetivo", "Estado objetivo alineado a la estrategia de negocio, con principios y estándares de arquitectura."),
            ("Roadmap multianual", "Hoja de ruta priorizada por valor, riesgo y dependencias, organizada en horizontes de ejecución."),
            ("Caso de negocio", "Modelo de costos, beneficios y riesgos que sustenta la decisión ante el consejo o el comité."),
            ("Due diligence tecnológico", "Evaluación de activos y riesgos tecnológicos en procesos de inversión, fusión o adquisición."),
            ("Modelo operativo de TI", "Diseño de organización, procesos y estrategia de sourcing para ejecutar el plan."),
        ],
        "approach": [
            ("Entender", "Entrevistas con la dirección y las áreas clave, revisión documental e inventario del estado actual."),
            ("Evaluar", "Análisis de brechas frente a las necesidades del negocio y las prácticas de referencia del sector."),
            ("Diseñar", "Arquitectura objetivo y alternativas evaluadas con criterios explícitos."),
            ("Priorizar", "Roadmap y caso de negocio presentados a la dirección para decisión."),
        ],
        "deliverables": [
            "Informe ejecutivo de diagnóstico",
            "Mapa de arquitectura actual y objetivo",
            "Matriz de riesgos tecnológicos priorizada",
            "Roadmap multianual por horizontes",
            "Caso de negocio con escenarios",
            "Recomendación de modelo operativo y sourcing",
        ],
        "models": ["Diagnóstico estratégico de dos semanas", "Proyecto de estrategia a precio cerrado", "Acompañamiento ejecutivo continuo"],
        "outcomes": [
            ("Claridad", "Una visión compartida de hacia dónde va la tecnología y por qué."),
            ("Priorización por valor", "Cada iniciativa justificada por su impacto en crecimiento, eficiencia o riesgo."),
            ("Continuidad hacia la ejecución", "La estrategia que diseñamos es la misma que podemos ejecutar y de la que respondemos."),
        ],
        "faqs": [
            ("¿En qué se diferencian de una consultora de estrategia tradicional?", "Integramos asesoría y ejecución: las recomendaciones se diseñan para ser ejecutables y podemos responder por su implementación."),
            ("¿Cuánto dura un diagnóstico?", "El diagnóstico estratégico inicial dura dos semanas. Los proyectos de arquitectura y roadmap se dimensionan según el alcance."),
            ("¿Sus recomendaciones son independientes de fabricantes?", "Sí. No dependen de acuerdos comerciales con proveedores de tecnología."),
        ],
        "related": ["cloud-multicloud", "data-ai", "cyber-trust"],
    },
    {
        "slug": "staff-augmentation",
        "name": "Staff Augmentation",
        "sub": "Talento especializado",
        "plane": "nucleo",
        "icon": "users",
        "short": "Talento senior validado, técnica y culturalmente, con reemplazo garantizado.",
        "tagline": "Talento senior que se integra a su equipo desde la primera semana.",
        "lede": "Profesionales validados técnica y culturalmente que amplían la capacidad de sus equipos, con seguimiento de Oakmont durante toda la asignación y reemplazo garantizado.",
        "problems": [
            ("Vacantes críticas sin cubrir", "Perfiles especializados que tardan meses en contratarse mientras los proyectos esperan."),
            ("Picos de demanda temporales", "Necesidades de capacidad que no justifican crecer la plantilla permanente."),
            ("Dependencia de personas clave", "Proyectos expuestos cuando una persona sale antes de tiempo y no hay respaldo."),
        ],
        "offerings": [
            ("Ingeniería de software", "Desarrollo backend, frontend y móvil, arquitectura de software e integración."),
            ("Cloud y DevOps", "Arquitectos cloud, ingenieros de plataforma, SRE y especialistas FinOps."),
            ("Datos e IA", "Ingeniería de datos, analítica, ciencia de datos y MLOps."),
            ("Calidad y seguridad", "QA manual y automatizado, pruebas de desempeño y especialistas en ciberseguridad."),
            ("Gestión y negocio", "Project managers, scrum masters, product owners y analistas de negocio."),
        ],
        "approach": [
            ("Perfilamiento", "Definimos con usted el rol, el contexto del equipo y los criterios de éxito."),
            ("Validación", "Evaluación técnica práctica y entrevista de ajuste cultural antes de presentar candidatos."),
            ("Incorporación", "Integración acompañada a sus herramientas, procesos y equipo."),
            ("Seguimiento", "Revisiones periódicas de desempeño y reemplazo garantizado si el perfil no cumple."),
        ],
        "deliverables": [
            "Candidatos validados por rol",
            "Reporte de evaluación técnica de cada candidato",
            "Plan de incorporación",
            "Revisiones periódicas de desempeño",
            "Reemplazo garantizado",
        ],
        "models": ["Asignación individual por periodo definido", "Equipo extendido", "Asignación con opción de contratación directa"],
        "outcomes": [
            ("Cobertura más rápida", "Candidatos ya validados en lugar de procesos de reclutamiento desde cero."),
            ("Riesgo controlado", "Seguimiento continuo y reemplazo garantizado en cada asignación."),
            ("Flexibilidad", "Capacidad que crece o se reduce según la demanda real de sus proyectos."),
        ],
        "faqs": [
            ("¿Cómo validan a los candidatos?", "Cada candidato resuelve una evaluación técnica práctica sobre problemas reales del rol y tiene una entrevista de ajuste cultural con un líder senior de Oakmont."),
            ("¿Qué pasa si el perfil no funciona?", "Gestionamos el reemplazo sin costo adicional de reclutamiento y cuidamos la transferencia de contexto."),
            ("¿Las asignaciones pueden ser presenciales?", "Sí. Pueden ser presenciales, híbridas o remotas, según sus políticas."),
        ],
        "related": ["fabrica-de-software", "quality-engineering", "data-ai"],
    },
    {
        "slug": "cloud-multicloud",
        "name": "Cloud / Multicloud",
        "sub": "Modernización en la nube",
        "plane": "nucleo",
        "icon": "cloud",
        "short": "Estrategia óptima por aplicación bajo el marco 7R — sin recetas únicas.",
        "tagline": "La nube correcta para cada aplicación, no la misma receta para todas.",
        "lede": "Definimos y ejecutamos la estrategia de nube aplicación por aplicación bajo el marco 7R, sobre AWS, Microsoft Azure y Google Cloud, con independencia de fabricante.",
        "problems": [
            ("Migraciones que no generan ahorro", "Cargas trasladadas tal cual que replican en la nube los costos e ineficiencias del centro de datos."),
            ("Dependencia de un solo proveedor", "Arquitecturas difíciles de mover que reducen su capacidad de negociación."),
            ("Infraestructura al final de su vida útil", "Renovaciones que obligan a decidir con poco tiempo y poca información."),
        ],
        "offerings": [
            ("Estrategia y evaluación de portafolio", "Análisis de cada aplicación para decidir su disposición bajo el marco 7R."),
            ("Landing zones y fundamentos", "Cuentas, redes, identidad, seguridad y gobierno listos para operar a escala."),
            ("Migración", "Olas de migración planificadas, con pruebas, ventanas de corte y planes de reversa."),
            ("Modernización cloud-native", "Contenedores, serverless y servicios administrados donde aportan valor real."),
            ("Arquitectura multicloud e híbrida", "Cargas distribuidas entre nubes y centros de datos propios con un gobierno común."),
        ],
        "seven_r": [
            ("Retain", "Mantener la aplicación donde está, por ahora."),
            ("Retire", "Dar de baja lo que ya no aporta valor."),
            ("Rehost", "Mover a infraestructura en la nube sin cambios."),
            ("Relocate", "Trasladar plataformas completas, como entornos virtualizados, sin modificarlas."),
            ("Replatform", "Ajustes puntuales para aprovechar servicios administrados."),
            ("Repurchase", "Sustituir por una solución SaaS."),
            ("Refactor", "Rediseñar para aprovechar capacidades cloud-native."),
        ],
        "approach": [
            ("Inventario", "Descubrimiento de aplicaciones, dependencias y costos actuales."),
            ("Disposición 7R", "Decisión por aplicación con criterios de valor, riesgo y esfuerzo."),
            ("Fundamentos", "Landing zone, seguridad y gobierno antes de la primera migración."),
            ("Olas de ejecución", "Migración y modernización por olas, midiendo costo y desempeño en cada una."),
        ],
        "deliverables": [
            "Inventario de aplicaciones y dependencias",
            "Disposición 7R por aplicación",
            "Arquitectura de landing zone",
            "Plan de migración por olas",
            "Modelo de costos de nube proyectado",
            "Runbooks de operación",
        ],
        "models": ["Evaluación de portafolio a precio cerrado", "Programa de migración por olas", "Célula de modernización dedicada"],
        "outcomes": [
            ("Costo alineado al uso", "Infraestructura dimensionada a la demanda real de cada aplicación."),
            ("Independencia", "Arquitecturas portables que conservan su capacidad de negociación."),
            ("Resiliencia", "Diseños con alta disponibilidad y recuperación ante desastres desde el inicio."),
        ],
        "faqs": [
            ("¿Con qué nubes trabajan?", "Con AWS, Microsoft Azure y Google Cloud, con quienes mantenemos alianzas. Recomendamos la que mejor se ajusta a cada carga."),
            ("¿Siempre recomiendan migrar a la nube?", "No. Retain y Retire también son decisiones válidas; recomendamos lo que tiene sentido para cada aplicación."),
            ("¿Quién opera las cargas después de migrar?", "Su equipo, con transferencia de conocimiento, o nuestro servicio de Cloud Operations."),
        ],
        "related": ["cloud-operations", "cyber-trust", "strategy-advisory"],
    },
    {
        "slug": "data-ai",
        "name": "Data & AI",
        "sub": "Inteligencia artificial y datos",
        "plane": "habilitadora",
        "icon": "sparkles",
        "short": "Del dato a la decisión y de la IA a la ventaja operativa, con ROI demostrable.",
        "tagline": "Del dato a la decisión, y de la IA a la ventaja operativa.",
        "lede": "Construimos plataformas de datos gobernadas y casos de uso de inteligencia artificial con retorno demostrable, desde la ingesta del dato hasta el modelo en producción.",
        "problems": [
            ("Datos fragmentados", "Información repartida en sistemas que no conversan y versiones distintas de la misma verdad."),
            ("Pilotos de IA que no llegan a producción", "Pruebas de concepto prometedoras sin ruta a operación ni medición de valor."),
            ("Reportes que llegan tarde", "Decisiones tomadas con información de semanas atrás y procesos manuales de consolidación."),
        ],
        "offerings": [
            ("Plataformas de datos modernas", "Ingesta, almacenamiento y modelado en arquitecturas lakehouse sobre la nube que usted elija."),
            ("Gobierno y calidad de datos", "Catálogo, linaje, calidad y políticas de acceso para un dato confiable y auditable."),
            ("Analítica y visualización", "Tableros ejecutivos y operativos construidos sobre una sola fuente de verdad."),
            ("IA aplicada", "Modelos predictivos y de optimización para pronóstico, riesgo, fraude y eficiencia operativa."),
            ("IA generativa empresarial", "Asistentes y automatización sobre su propia información, con controles de seguridad y privacidad."),
            ("MLOps", "Despliegue, monitoreo y reentrenamiento de modelos como cualquier otro software en producción."),
        ],
        "approach": [
            ("Caso de uso", "Selección y priorización por valor de negocio y viabilidad con los datos disponibles."),
            ("Fundamentos de datos", "Ingesta, calidad y gobierno mínimos necesarios para el caso de uso."),
            ("Prototipo medible", "Solución acotada con métricas de negocio acordadas antes de construir."),
            ("Producción", "Despliegue, monitoreo y operación con el mismo rigor que el resto del software."),
        ],
        "deliverables": [
            "Portafolio de casos de uso priorizado",
            "Arquitectura de datos objetivo",
            "Pipelines de datos documentados",
            "Modelos en producción con monitoreo",
            "Tableros y métricas de impacto",
            "Políticas de gobierno y acceso a datos",
        ],
        "models": ["Evaluación de casos de uso a precio cerrado", "Proyecto de plataforma de datos", "Célula de datos e IA dedicada"],
        "outcomes": [
            ("Decisiones más rápidas", "Información confiable disponible cuando se necesita."),
            ("Retorno demostrable", "Cada caso de uso con métricas de negocio definidas desde el inicio."),
            ("IA responsable", "Privacidad, trazabilidad y control humano diseñados desde el principio."),
        ],
        "faqs": [
            ("¿Por dónde conviene empezar con IA?", "Por un caso de uso con valor medible y datos disponibles. Evitamos pilotos sin ruta a producción."),
            ("¿Cómo protegen la información sensible?", "Con controles de acceso, anonimización y trazabilidad desde el diseño, junto con nuestra práctica de Cyber & Trust."),
            ("¿Necesitamos una plataforma de datos antes de usar IA?", "No siempre. Evaluamos si los datos actuales bastan para el caso de uso y construimos la plataforma de forma incremental."),
        ],
        "related": ["strategy-advisory", "cyber-trust", "cloud-multicloud"],
    },
    {
        "slug": "cyber-trust",
        "name": "Cyber & Trust",
        "sub": "Ciberseguridad",
        "plane": "habilitadora",
        "icon": "shield-check",
        "short": "Seguridad por diseño — no como un control de última hora.",
        "tagline": "Seguridad por diseño, no como un control de última hora.",
        "lede": "Integramos la seguridad en la arquitectura, el desarrollo y la operación para reducir la exposición de su organización sin frenar la entrega.",
        "problems": [
            ("Seguridad al final del ciclo", "Hallazgos que aparecen justo antes de salir a producción y retrasan cada liberación."),
            ("Una superficie de ataque que crece", "Nube, APIs y accesos de terceros que se expanden más rápido que los controles."),
            ("Presión regulatoria y de auditoría", "Requisitos de cumplimiento que exigen evidencia continua, no esfuerzos de última hora."),
        ],
        "offerings": [
            ("Evaluación de postura de seguridad", "Diagnóstico de controles, riesgos y madurez frente a marcos de referencia."),
            ("Arquitectura segura y Zero Trust", "Diseño de redes, identidades y accesos bajo el principio de mínimo privilegio."),
            ("DevSecOps", "Análisis de código, dependencias y contenedores integrados al pipeline de entrega."),
            ("Seguridad en la nube", "Configuración segura, monitoreo de postura y protección de cargas en AWS, Azure y Google Cloud."),
            ("Identidades y accesos", "Gestión del ciclo de vida de identidades, autenticación robusta y accesos privilegiados."),
            ("Pruebas de penetración y vulnerabilidades", "Pruebas controladas y gestión continua de vulnerabilidades hasta su remediación."),
            ("Cumplimiento y riesgo", "Alineación a marcos como ISO/IEC 27001, NIST CSF o PCI DSS, según aplique a su organización."),
        ],
        "approach": [
            ("Evaluar", "Postura actual, activos críticos y exposición, con hallazgos clasificados por riesgo."),
            ("Priorizar", "Plan de remediación ordenado por impacto en el negocio y esfuerzo."),
            ("Remediar", "Implementación de controles técnicos y de proceso, integrados a la operación."),
            ("Verificar", "Pruebas, evidencia de cumplimiento y mejora continua."),
        ],
        "deliverables": [
            "Evaluación de postura con hallazgos priorizados",
            "Arquitectura de seguridad objetivo",
            "Plan de remediación",
            "Controles integrados al pipeline de entrega",
            "Informes de pruebas de penetración",
            "Matriz de cumplimiento con evidencia",
        ],
        "models": ["Evaluación de seguridad a precio cerrado", "Programa de remediación", "Especialistas dedicados de seguridad"],
        "outcomes": [
            ("Exposición reducida", "Riesgos críticos identificados, priorizados y atendidos."),
            ("Entrega sin fricción", "Controles automatizados que no frenan las liberaciones."),
            ("Cumplimiento demostrable", "Evidencia lista para auditorías internas y externas."),
        ],
        "faqs": [
            ("¿Pueden trabajar con nuestro equipo de seguridad?", "Sí. Complementamos a su equipo con capacidades especializadas y le transferimos las prácticas que implementamos."),
            ("¿Con qué marcos de referencia trabajan?", "Alineamos los controles a los marcos que aplican a su organización, como ISO/IEC 27001, NIST CSF o PCI DSS."),
            ("¿Realizan pruebas de penetración?", "Sí, con alcance, ventanas y reglas de enfrentamiento acordadas por escrito antes de iniciar."),
        ],
        "related": ["cloud-operations", "fabrica-de-software", "cloud-multicloud"],
    },
    {
        "slug": "cloud-operations",
        "name": "Cloud Operations",
        "sub": "DevOps · SRE · FinOps",
        "plane": "habilitadora",
        "icon": "activity",
        "short": "Plataformas modernas con confiabilidad y eficiencia de costo demostrables.",
        "tagline": "Plataformas disponibles que cuestan lo que deben costar.",
        "lede": "Operamos y mejoramos sus plataformas con prácticas de DevOps, Site Reliability Engineering y FinOps: confiabilidad medible y eficiencia de costo demostrable.",
        "problems": [
            ("Incidentes recurrentes", "Las mismas fallas vuelven y el equipo vive apagando incendios."),
            ("Una factura de nube que crece sin control", "Costos sin visibilidad por servicio ni responsables claros."),
            ("Despliegues manuales y riesgosos", "Liberaciones que requieren ventanas largas y dependen de pocas personas."),
        ],
        "offerings": [
            ("DevOps y automatización", "Pipelines, infraestructura como código y entornos reproducibles."),
            ("Site Reliability Engineering", "Objetivos de nivel de servicio, observabilidad y respuesta estructurada a incidentes."),
            ("FinOps", "Visibilidad de costos por servicio y equipo, asignación y optimización continua."),
            ("Observabilidad", "Métricas, trazas y registros correlacionados para detectar problemas antes que el usuario."),
            ("Operación gestionada", "Monitoreo, gestión de incidentes y cambios, y mantenimiento de plataforma con alcance acordado."),
        ],
        "approach": [
            ("Línea base", "Disponibilidad, costos y frecuencia de despliegue actuales, medidos."),
            ("Estabilizar", "Atención de las causas raíz de los incidentes más frecuentes."),
            ("Automatizar", "Despliegues, infraestructura y respuestas operativas repetibles."),
            ("Optimizar", "Revisión continua de confiabilidad y costo con el negocio."),
        ],
        "deliverables": [
            "Objetivos de nivel de servicio acordados con el negocio",
            "Plataforma de observabilidad configurada",
            "Infraestructura como código versionada",
            "Tablero de costos por servicio y equipo",
            "Runbooks y procedimientos de respuesta",
            "Reporte periódico de niveles de servicio",
        ],
        "models": ["Evaluación operativa a precio cerrado", "Equipo de plataforma dedicado", "Servicio gestionado con niveles de servicio"],
        "outcomes": [
            ("Confiabilidad", "Disponibilidad medida contra objetivos acordados con el negocio."),
            ("Eficiencia de costo", "Gasto en nube visible, asignado y optimizado de forma continua."),
            ("Despliegues frecuentes", "Liberaciones automatizadas, pequeñas y de menor riesgo."),
        ],
        "faqs": [
            ("¿Qué incluye la operación gestionada?", "Monitoreo, gestión de incidentes y cambios, mantenimiento de plataforma y reporte de niveles de servicio, con el alcance y los horarios acordados en contrato."),
            ("¿Cómo reducen el costo de nube?", "Con visibilidad por servicio y equipo, ajuste de capacidad, compromisos de uso y eliminación de recursos ociosos."),
            ("¿Operan en varias nubes?", "Sí. Operamos cargas en AWS, Microsoft Azure y Google Cloud, y en entornos híbridos."),
        ],
        "related": ["cloud-multicloud", "cyber-trust", "quality-engineering"],
    },
    {
        "slug": "quality-engineering",
        "name": "Quality Engineering",
        "sub": "Calidad y pruebas de software",
        "plane": "habilitadora",
        "icon": "badge-check",
        "short": "Que el software cumpla antes de impactar al usuario y al negocio.",
        "tagline": "Que el software cumpla antes de impactar al usuario y al negocio.",
        "lede": "Estrategia de calidad, automatización de pruebas y pruebas especializadas integradas al ciclo de entrega, para liberar con frecuencia y con confianza.",
        "problems": [
            ("Defectos que llegan a producción", "Errores que descubre el cliente y que cuestan más corregir cuanto más tarde aparecen."),
            ("Pruebas manuales que frenan las liberaciones", "Ciclos de regresión largos que limitan la frecuencia de entrega."),
            ("Desempeño incierto bajo carga", "Sistemas que no se han probado en las condiciones reales de mayor demanda."),
        ],
        "offerings": [
            ("Estrategia y gobierno de calidad", "Modelo de pruebas, criterios de aceptación y métricas de calidad por producto."),
            ("Automatización de pruebas", "Pruebas de interfaz, API e integración ejecutadas en cada cambio dentro del pipeline."),
            ("Pruebas de desempeño y carga", "Simulación de demanda real para validar capacidad y tiempos de respuesta."),
            ("Pruebas de seguridad de aplicaciones", "Análisis estático y dinámico coordinado con nuestra práctica de Cyber & Trust."),
            ("Accesibilidad y usabilidad", "Verificación de que el producto funcione para todas las personas que lo usan."),
            ("QA como servicio", "Equipos de calidad dedicados con niveles de servicio acordados."),
        ],
        "approach": [
            ("Evaluar madurez", "Prácticas, cobertura y defectos actuales, medidos."),
            ("Diseñar la estrategia", "Qué probar, cómo y en qué etapa, según el riesgo de cada componente."),
            ("Automatizar", "Pruebas repetibles integradas al flujo de entrega."),
            ("Medir", "Indicadores de calidad visibles para el equipo y la dirección."),
        ],
        "deliverables": [
            "Estrategia de pruebas por producto",
            "Suites automatizadas integradas al pipeline",
            "Informes de pruebas de desempeño",
            "Tablero de métricas de calidad",
            "Criterios de aceptación y de salida a producción",
        ],
        "models": ["Evaluación de madurez a precio cerrado", "Equipo de QA dedicado", "QA como servicio con niveles de servicio"],
        "outcomes": [
            ("Menos defectos en producción", "Errores detectados cuando corregirlos cuesta menos."),
            ("Liberaciones más frecuentes", "Regresión automatizada en lugar de ciclos manuales largos."),
            ("Confianza para cambiar", "Equipos que pueden evolucionar el software sin miedo a romperlo."),
        ],
        "faqs": [
            ("¿Automatizan todas las pruebas?", "No. Automatizamos lo que se repite y aporta valor; las pruebas exploratorias siguen siendo humanas."),
            ("¿Pueden probar software desarrollado por otros proveedores?", "Sí. Nuestra práctica de calidad es independiente de quién desarrolle el software."),
            ("¿Qué herramientas utilizan?", "Las que mejor se integren con su stack y su pipeline; no imponemos una herramienta única."),
        ],
        "related": ["fabrica-de-software", "cloud-operations", "staff-augmentation"],
    },
]

# --------------------------------------------------------------------------
# Industries
# --------------------------------------------------------------------------
INDUSTRIES = [
    {
        "slug": "servicios-financieros",
        "name": "Servicios financieros",
        "icon": "landmark",
        "tagline": "Modernizar el núcleo sin poner en riesgo la operación.",
        "lede": "Bancos, instituciones financieras no bancarias y fintechs necesitan competir con experiencias digitales mientras operan sistemas centrales críticos, regulados y de alta disponibilidad.",
        "context": [
            "En servicios financieros, la tecnología es el producto. Cada nuevo crédito, cuenta o medio de pago depende de sistemas centrales que deben evolucionar sin interrumpir una operación que no se detiene.",
            "Acompañamos a las instituciones a desacoplar su núcleo transaccional por etapas, con la seguridad y el control que exige el regulador.",
        ],
        "challenges": [
            ("Núcleos transaccionales legados", "Costosos de operar, difíciles de cambiar y dependientes de pocos especialistas."),
            ("Exigencia regulatoria", "Requisitos de seguridad, continuidad y reporte que deben cumplirse en cada cambio."),
            ("Competencia digital", "Nuevos participantes que lanzan productos en semanas, no en trimestres."),
            ("Seguridad y fraude", "Amenazas cada vez más sofisticadas sobre canales digitales y APIs."),
        ],
        "help": [
            ("cloud-multicloud", "Modernización del núcleo bajo el marco 7R, aplicación por aplicación."),
            ("fabrica-de-software", "Células que construyen nuevos productos sobre APIs gobernadas."),
            ("cyber-trust", "Seguridad por diseño y evidencia continua de cumplimiento."),
            ("data-ai", "Modelos de riesgo y detección de fraude con datos gobernados."),
        ],
        "case": "modernizacion-nucleo-transaccional",
    },
    {
        "slug": "retail-y-consumo",
        "name": "Retail y consumo",
        "icon": "shopping-bag",
        "tagline": "Disponibilidad y experiencia cuando más importan.",
        "lede": "Cadenas comerciales, marcas de consumo y comercio electrónico dependen de plataformas que deben responder en los momentos de mayor demanda y con márgenes que no admiten desperdicio.",
        "context": [
            "En retail, los picos de demanda concentran buena parte de los ingresos del año. Una plataforma que falla en ese momento no solo pierde ventas: pierde clientes.",
            "Ayudamos a diseñar y operar plataformas que escalan con la demanda y a convertir los datos de venta e inventario en decisiones.",
        ],
        "challenges": [
            ("Picos de demanda", "Temporadas y campañas que multiplican el tráfico en horas."),
            ("Experiencia omnicanal", "Tienda, comercio electrónico y aplicaciones que deben comportarse como un solo canal."),
            ("Inventario y abastecimiento", "Decisiones de compra y distribución que dependen de información oportuna."),
            ("Márgenes estrechos", "Costo de plataforma que debe crecer menos que las ventas."),
        ],
        "help": [
            ("cloud-operations", "SRE y observabilidad para mantener la disponibilidad en los picos."),
            ("cloud-multicloud", "Rearquitectura cloud-native que escala con la demanda."),
            ("data-ai", "Pronóstico de demanda y analítica de inventario."),
            ("fabrica-de-software", "Evolución continua de canales digitales."),
        ],
        "case": "disponibilidad-retail-cloud-native",
    },
    {
        "slug": "salud-y-seguros",
        "name": "Salud y seguros",
        "icon": "heart-pulse",
        "tagline": "Datos gobernados para decidir mejor y lanzar nuevos servicios.",
        "lede": "Aseguradoras, proveedores de salud y administradores de beneficios gestionan información sensible y procesos intensivos en documentos que piden datos confiables y automatización responsable.",
        "context": [
            "En salud y seguros, la información está dispersa entre pólizas, expedientes, reclamaciones y proveedores. Unificarla sin comprometer la privacidad es la condición para decidir mejor.",
            "Construimos plataformas de datos gobernadas y aplicamos IA sobre procesos como suscripción y reclamaciones, con controles de privacidad desde el diseño.",
        ],
        "challenges": [
            ("Datos fragmentados", "Información de clientes, pólizas y siniestros repartida en sistemas que no se integran."),
            ("Privacidad de datos sensibles", "Información personal y de salud que exige controles estrictos de acceso y uso."),
            ("Procesos intensivos en documentos", "Suscripción y reclamaciones que dependen de revisión manual."),
            ("Sistemas centrales rígidos", "Plataformas de pólizas o expedientes difíciles de adaptar a nuevos productos."),
        ],
        "help": [
            ("data-ai", "Plataforma de datos gobernada y analítica avanzada."),
            ("cyber-trust", "Privacidad y control de accesos sobre información sensible."),
            ("fabrica-de-software", "Integración de sistemas centrales mediante APIs."),
            ("quality-engineering", "Pruebas rigurosas en procesos regulados."),
        ],
        "case": "plataforma-datos-salud-seguros",
    },
]

# --------------------------------------------------------------------------
# Case studies
# --------------------------------------------------------------------------
CASES = [
    {
        "slug": "modernizacion-nucleo-transaccional",
        "n": "01",
        "industry": "servicios-financieros",
        "title": "Time-to-market acelerado y reducción sostenida del costo de plataforma.",
        "summary": "Modernización multicloud de un núcleo transaccional legado, con fábrica de software gestionada.",
        "context": "Una institución de servicios financieros operaba su núcleo transaccional sobre una plataforma legada, costosa de mantener y difícil de cambiar. Cada nuevo producto requería modificar componentes acoplados y coordinar ventanas de liberación extensas.",
        "challenge": [
            "Núcleo transaccional legado, costoso de operar y lento para evolucionar.",
            "Dependencia de pocos especialistas para cada cambio.",
            "Requisitos de continuidad y seguridad que no admitían interrupciones.",
        ],
        "approach": [
            ("Define", "Diagnóstico del portafolio y disposición 7R por componente, con un caso de negocio aprobado por la dirección."),
            ("Evolve", "Desacoplamiento progresivo del núcleo mediante APIs gobernadas y migración por olas."),
            ("Deliver", "Fábrica de software gestionada con niveles de servicio y un comité de seguimiento ejecutivo."),
        ],
        "solution": [
            "Arquitectura de servicios desacoplados sobre una landing zone multicloud.",
            "Capa de APIs gobernadas para exponer capacidades del núcleo a nuevos canales.",
            "Pipelines de integración y despliegue continuos con controles de seguridad integrados.",
            "Pruebas automatizadas de regresión sobre los flujos transaccionales críticos.",
        ],
        "results": [
            "Time-to-market acelerado para nuevos productos.",
            "Reducción sostenida del costo de plataforma.",
            "Componentes que evolucionan de forma independiente.",
            "Un solo responsable de la estrategia a la operación.",
        ],
        "services": ["cloud-multicloud", "fabrica-de-software", "cyber-trust", "quality-engineering"],
    },
    {
        "slug": "disponibilidad-retail-cloud-native",
        "n": "02",
        "industry": "retail-y-consumo",
        "title": "Alta disponibilidad en operación y despliegues de semanas a días.",
        "summary": "Rearquitectura cloud-native con observabilidad y prácticas SRE para una operación de retail.",
        "context": "Una organización de retail y consumo enfrentaba picos de demanda que comprometían la disponibilidad de sus canales digitales justo en los momentos de mayor venta. Las liberaciones eran manuales y se concentraban en ventanas poco frecuentes.",
        "challenge": [
            "Picos de demanda que comprometían la disponibilidad y la experiencia digital.",
            "Despliegues manuales, poco frecuentes y de alto riesgo.",
            "Poca visibilidad del comportamiento de la plataforma en producción.",
        ],
        "approach": [
            ("Define", "Línea base de disponibilidad, desempeño y frecuencia de despliegue, y objetivos de nivel de servicio acordados con el negocio."),
            ("Evolve", "Rearquitectura cloud-native de los componentes críticos para escalar con la demanda."),
            ("Deliver", "Operación con prácticas SRE, observabilidad de extremo a extremo y despliegues automatizados."),
        ],
        "solution": [
            "Componentes críticos contenedorizados con escalamiento automático.",
            "Observabilidad con métricas, trazas y registros correlacionados.",
            "Pipelines de despliegue automatizados con liberaciones progresivas.",
            "Pruebas de carga previas a cada temporada de alta demanda.",
        ],
        "results": [
            "Alta disponibilidad en operación durante los picos de demanda.",
            "Despliegues que pasaron de semanas a días.",
            "Detección temprana de problemas antes de que afecten al cliente.",
            "Objetivos de nivel de servicio compartidos entre negocio y tecnología.",
        ],
        "services": ["cloud-multicloud", "cloud-operations", "quality-engineering"],
    },
    {
        "slug": "plataforma-datos-salud-seguros",
        "n": "03",
        "industry": "salud-y-seguros",
        "title": "Ciclo de decisión más corto y nuevos servicios de datos en producción.",
        "summary": "Plataforma de datos gobernada con analítica avanzada e IA aplicada en salud y seguros.",
        "context": "Una organización de salud y seguros tenía la información de clientes, pólizas y reclamaciones distribuida en sistemas aislados. Consolidarla requería procesos manuales y las decisiones se tomaban con información desactualizada.",
        "challenge": [
            "Datos fragmentados que frenaban decisiones y el lanzamiento de nuevos servicios.",
            "Información sensible que exigía controles estrictos de privacidad.",
            "Procesos de análisis manuales y lentos.",
        ],
        "approach": [
            ("Define", "Priorización de casos de uso por valor y viabilidad, y arquitectura de datos objetivo."),
            ("Evolve", "Construcción incremental de la plataforma de datos con gobierno y calidad desde el inicio."),
            ("Deliver", "Analítica y modelos de IA en producción, con monitoreo y métricas de impacto."),
        ],
        "solution": [
            "Plataforma de datos con catálogo, linaje y políticas de acceso.",
            "Integración de fuentes de clientes, pólizas y reclamaciones.",
            "Tableros ejecutivos sobre una sola fuente de verdad.",
            "Modelos de IA aplicada con controles de privacidad y trazabilidad.",
        ],
        "results": [
            "Ciclo de decisión más corto.",
            "Nuevos servicios de datos en producción.",
            "Datos gobernados con trazabilidad de origen a uso.",
            "Casos de IA medidos con métricas de negocio.",
        ],
        "services": ["data-ai", "cyber-trust", "fabrica-de-software"],
    },
]

# --------------------------------------------------------------------------
# Approach (Enfoque) page
# --------------------------------------------------------------------------
HORIZONS = [
    ("01", "Define", "Estrategia y asesoría", "Diagnóstico, arquitectura objetivo y hoja de ruta priorizada por valor.",
     ["Diagnóstico del estado actual", "Arquitectura objetivo", "Roadmap multianual", "Caso de negocio"]),
    ("02", "Evolve", "Modernización y arquitectura", "Rediseño de capacidades y transición del estado actual al estado objetivo.",
     ["Modernización de aplicaciones", "Migración y fundamentos de nube", "Plataformas de datos", "Arquitectura de seguridad"]),
    ("03", "Deliver", "Ingeniería y operación", "Ingeniería, integración, despliegue y operación gestionada.",
     ["Fábrica de software", "Talento especializado", "Operación de plataformas", "Calidad continua"]),
]

LAYER = [
    ("Gobierno", "Un comité, un responsable y un tablero de indicadores para toda la iniciativa."),
    ("Calidad", "Criterios de calidad definidos antes de construir y verificados en cada entrega."),
    ("Seguridad", "Controles de seguridad integrados desde el diseño, no añadidos al final."),
    ("Innovación", "Evaluación continua de tecnologías emergentes, incluida la IA, con criterio de negocio."),
]

PHASES = [
    ("01", "Assess", "Entendimiento del negocio, el reto y el estado actual.",
     "Entrevistas con la dirección y los equipos, revisión de arquitectura y definición del problema a resolver."),
    ("02", "Design", "Alcance a la medida, modelo de entrega y métricas de éxito.",
     "Propuesta con alcance, equipo, calendario, modelo contractual e indicadores acordados antes de iniciar."),
    ("03", "Execute", "Ejecución gestionada con transparencia y comunicación continua.",
     "Entregas incrementales, comité de seguimiento periódico y reporte ejecutivo de avance, riesgos y decisiones."),
    ("04", "Sustain", "Medición de impacto, iteración y evolución continua.",
     "Medición contra las métricas de éxito, transferencia de conocimiento y plan de evolución."),
]

GOVERNANCE = [
    ("Comité directivo", "Comité ejecutivo con el patrocinador del cliente para decisiones de alcance, prioridad y riesgo."),
    ("Gestión de riesgos", "Registro de riesgos vivo, con responsables y planes de mitigación revisados en cada comité."),
    ("Reporte ejecutivo", "Tablero de avance, calidad, costo y niveles de servicio, con la misma información para todos."),
    ("Un solo responsable", "Un responsable de Oakmont que responde por el resultado de principio a fin."),
]

CONTRACTS = [
    ("Proyecto", "Alcance y entregables definidos, a precio cerrado.", "Iniciativas con objetivos y alcance claros."),
    ("Capacidad dedicada", "Una célula de Oakmont con capacidad mensual y prioridades que usted define.", "Backlogs continuos que evolucionan con el negocio."),
    ("Talento especializado", "Profesionales validados que se integran a sus equipos.", "Cubrir perfiles específicos o picos de demanda."),
    ("Servicio gestionado", "Operación de un servicio con niveles de servicio acordados.", "Aplicaciones o plataformas que requieren operación continua."),
]

MEASURES = [
    ("Time-to-market", "Cuánto tarda una idea en llegar a producción."),
    ("Costo", "Cuánto cuesta construir, operar y evolucionar la tecnología."),
    ("Riesgo", "Cuánta exposición operativa, de seguridad y regulatoria se reduce."),
]

# --------------------------------------------------------------------------
# About
# --------------------------------------------------------------------------
REASONS = [
    ("01", "De la asesoría a la ingeniería, bajo un solo techo", "Respondemos por la estrategia que ejecutamos. Quien diseña la solución forma parte de quien la construye y la opera."),
    ("02", "Talento senior validado", "Experiencia real en entornos de alta exigencia. Cada profesional pasa una evaluación técnica práctica y de ajuste cultural."),
    ("03", "Neutralidad tecnológica y multicloud", "Independencia al servicio del negocio. Recomendamos la tecnología que conviene a cada caso, no la que conviene a un acuerdo comercial."),
    ("04", "IA e innovación embebidas", "Preparamos a la organización para el siguiente ciclo, incorporando IA donde genera valor medible."),
    ("05", "Responsabilidad por resultados", "Time-to-market, costo y riesgo como métricas de éxito, acordadas antes de empezar."),
]

DIAGNOSTIC = {
    "weeks": [
        ("Semana 1", "Entender", [
            "Sesión de arranque con el patrocinador y definición de objetivos",
            "Entrevistas con la dirección y las áreas clave",
            "Inventario de aplicaciones, infraestructura y datos",
            "Revisión de arquitectura, seguridad y operación",
        ]),
        ("Semana 2", "Priorizar", [
            "Análisis de brechas frente a los objetivos del negocio",
            "Identificación y priorización de riesgos",
            "Iniciativas recomendadas por horizonte",
            "Presentación ejecutiva de hallazgos",
        ]),
    ],
    "deliverables": [
        ("Informe ejecutivo", "Hallazgos principales y recomendaciones en lenguaje de negocio."),
        ("Mapa de arquitectura actual", "Vista de aplicaciones, integraciones, datos e infraestructura."),
        ("Riesgos priorizados", "Exposición operativa, de seguridad y regulatoria, ordenada por impacto."),
        ("Iniciativas por horizonte", "Qué hacer primero, qué después y por qué, en Define, Evolve y Deliver."),
    ],
    "needs": [
        "Un patrocinador ejecutivo con disponibilidad para dos sesiones",
        "Acceso a las personas clave de negocio y tecnología",
        "Documentación disponible de arquitectura, contratos y costos de TI",
    ],
}

# 🏛️ Suite Integral de Asistentes y Habilidades de la ECCL
### Escuela Canaria de Creación Literaria — 22 Años Formando Escritores (2004–2026)
> Repositorio oficial empaquetado como **Plugin de Antigravity y Claude Code**. Proporciona un ecosistema completo de **17 Asistentes Especializados**, **24 Skills Modulares**, **6 Protocolos Operativos (SOPs)** y el **Corpus Canónico** de la Escuela.

---

## ⚡ Instalación Rápida en 1 Comando

Para clonar e instalar toda la suite en tu equipo, abre tu terminal y ejecuta:

### 1. Clonar el repositorio
```bash
git clone https://github.com/albyojedadev/ECCL_Agentes.git
cd ECCL_Agentes
```

### 2. Ejecutar el instalador
**En Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install.ps1
```

**En Linux / macOS (Bash):**
```bash
chmod +x ./scripts/install.sh && ./scripts/install.sh
```

El instalador vinculará automáticamente el paquete en tu directorio de plugins (`~/.gemini/config/plugins/eccl-agent-suite`) y ejecutará las pruebas de salud y linters pre-vuelo asegurando que todo esté al 100% operativo.


---

## 👥 1. Catálogo Oficial de los 17 Asistentes

Los asistentes conservan la nomenclatura exacta y cercana que el equipo de la Escuela ya conoce, enriquecidos con nuevos agentes especializados:

| Asistente Oficial | Archivo en `agents/` | Origen / Función | Misión Principal |
| :--- | :--- | :---: | :--- |
| **`Coordinador de agentes de la ECCL`** | [`coordinador-de-agentes-de-la-eccl.md`](agents/coordinador-de-agentes-de-la-eccl.md) | GPT 00 (INDEX) | **Despacho y Moderación:** Orienta qué asistente usar y preside el Consejo Maestro. |
| **`Analista de Subvenciones y Licitaciones`** | [`analista-de-subvenciones-y-licitaciones.md`](agents/analista-de-subvenciones-y-licitaciones.md) | GPT 01 (Ayudas) | **Financiación Pública:** Detección y redacción técnica en *Modo Copycat* (ICDC, Cabildo, UE). |
| **`Analista de Datos Culturales y Educativos`** | [`analista-de-datos-culturales-y-educativos.md`](agents/analista-de-datos-culturales-y-educativos.md) | GPT 02 (Datos) | **Business Intelligence:** Umbrales de apertura de grupo, aforos y rentabilidad formativa. |
| **`Experto en la ECCL`** | [`experto-en-la-eccl.md`](agents/experto-en-la-eccl.md) | GPT 03 (Experto) | **Catálogo Canónico:** Información oficial de 73 cursos, 58 docentes, fechas y tarifas. |
| **`Consejo de alumnos sintéticos`** | [`consejo-de-alumnos-sinteticos.md`](agents/consejo-de-alumnos-sinteticos.md) | GPT 04 (Consejo) | **Simulación Focus Group:** 18 avatares reales para test de cursos, precios y objeciones. |
| **`Ghostwriter de Antonia Molinero`** | [`ghostwriter-de-antonia-molinero.md`](agents/ghostwriter-de-antonia-molinero.md) | GPT 05 (Ghostwriter) | **Voz Autoral:** Prólogos, cartas institucionales, ensayos y manifiestos en la voz de Antonia. |
| **`Crítico Literario de la ECCL`** | [`critico-literario-de-la-eccl.md`](agents/critico-literario-de-la-eccl.md) | GPT 06 (Crítico) | **Corrección Pedagógica Bifásica:** Informe Interno técnico + Comentario Externo afectivo. |
| **`Orientador de Admisiones y Alumnos`** | [`orientador-de-admisiones-y-alumnos.md`](agents/orientador-de-admisiones-y-alumnos.md) | Nuevo (Admisiones) | **Triaje Pedagógico:** Scoring de leads, atención de interesados e itinerarios formativos. |
| **`Compañero de Escritura y Hábito`** | [`companero-de-escritura-y-habito.md`](agents/companero-de-escritura-y-habito.md) | Nuevo (Alumnos) | **Tutor Socrático:** Desbloqueo creativo semanal y sostenimiento del hábito sin suplantar la voz. |
| **`Editor de Libros y Antologías`** | [`editor-de-libros-y-antologias.md`](agents/editor-de-libros-y-antologias.md) | Nuevo (Editorial) | **Edición Colectiva:** Selección de textos, revisión ortotipográfica y galeradas de imprenta. |
| **`Dinamizador de Comunidad y Clubes de Lectura`** | [`dinamizador-de-comunidad-y-clubes.md`](agents/dinamizador-de-comunidad-y-clubes.md) | Nuevo (Alumni) | **Fidelización:** Retos mensuales de escritura y dinamización de tertulias literarias. |
| **`Asesor de Propiedad Intelectual y Contratos`** | [`asesor-de-propiedad-intelectual.md`](agents/asesor-de-propiedad-intelectual.md) | Nuevo (Jurídico) | **Seguridad Legal:** Cesión no exclusiva para antologías, contratos de agencia y RGPD juvenil. |
| **`Asistente de Soporte y Aula Virtual`** | [`asistente-de-soporte-y-aula-virtual.md`](agents/asistente-de-soporte-y-aula-virtual.md) | Nuevo (Soporte) | **Campus Online:** Resolución de incidencias de Zoom, grabaciones en diferido y pagos. |
| **`Responsable de Comunicación y Prensa`** | [`responsable-de-comunicacion-y-prensa.md`](agents/responsable-de-comunicacion-y-prensa.md) | Nuevo (Prensa) | **Medios Culturales:** Notas de prensa en pirámide invertida y dossiers de presentación. |
| **`Gestor de Proyectos Institucionales y B2B`** | [`gestor-de-proyectos-institucionales-y-b2b.md`](agents/gestor-de-proyectos-institucionales-y-b2b.md) | Nuevo (Convenios) | **Proyectos a Medida:** Talleres para institutos (CEP), ayuntamientos y Escuela Portátil. |
| **`Diseñador Gráfico y Cartelería`** | [`disenador-grafico-y-carteleria.md`](agents/disenador-grafico-y-carteleria.md) | Nuevo (Diseño) | **Maquetación Publicitaria:** Cartelería A3/A4, posts de Instagram, Stories y banners web. |
| **`Guardián de Marca e Identidad Visual`** | [`guardian-de-marca-e-identidad-visual.md`](agents/guardian-de-marca-e-identidad-visual.md) | Nuevo (Branding) | **Auditoría Estética:** Control de paleta oficial, tipografía editorial y filtro anti-clichés de IA. |

---

## 🧩 2. Matriz de las 24 Skills Procedimentales

Cada skill es un módulo desacoplado (`skills/<id>/SKILL.md`) que se carga bajo demanda (Just-in-Time):

1. **`critica-pedagogica-literaria`**: Corrección bifásica con Informe Interno y Comentario Externo.
2. **`antonia-molinero-voice`**: Estilística autoral, objetos cotidianos y cadencia pausada.
3. **`verificacion-originalidad-y-voz-propia`**: Detección de tópicos y rescate de la voz genuina.
4. **`desbloqueo-creativo-socratico`**: Preguntas lúcidas para desatascar tramas y personajes.
5. **`seguimiento-habito-escritura`**: Diseño de rutinas sostenibles de escritura creativa.
6. **`curaduria-antologias-eccl`**: Selección armónica y edición de libros colectivos anuales.
7. **`dinamizacion-comunidad-literaria`**: Enunciados de retos mensuales y foros de debate.
8. **`contratos-editoriales-y-derechos-autor`**: Cesión de derechos no exclusiva y RGPD.
9. **`soporte-tecnico-aula-virtual`**: Guías de resolución paso a paso para Zoom y plataforma.
10. **`supervision-identidad-visual-eccl`**: Auditoría de paleta cromática, tipografías y safe zones.
11. **`diseno-carteleria-y-redes-eccl`**: Plantillas y directrices visuales para carteles y redes.
12. **`adaptacion-formatos-graficos-eccl`**: Redimensionamiento multiformato con márgenes seguros.
13. **`guion-reels-y-pildoras-literarias`**: Guiones audiovisuales breves con ganchos y consejos.
14. **`catalogo-academico-eccl`**: Búsqueda canónica de cursos, tarifas y docentes.
15. **`lead-scoring-eccl`**: Algoritmo de idoneidad y motivación de futuros alumnos.
16. **`orientacion-itinerarios-formativos`**: Mapeo del progreso del estudiante en la Escuela.
17. **`synthetic-audience-panel-eccl`**: Invocación de los 18 perfiles psicográficos reales.
18. **`cultural-grant-writer-es`**: Redacción técnica de memorias para concurrencia pública.
19. **`subvenciones-canarias-sync`**: Mapeo de pliegos del ICDC y cabildos insulares.
20. **`business-intelligence-cultural`**: Umbral de rentabilidad (break-even) y márgenes de grupo.
21. **`gestion-eventos-y-agenda-cultural`**: Organización de presentaciones, charlas y ferias del libro.
22. **`press-release-cultural-es`**: Redacción periodística de notas de prensa oficiales.
23. **`dossier-cultural-generator`**: Presentaciones ejecutivas para instituciones y socios.
24. **`propuestas-b2b-culturales`**: Proyectos formativos llave en mano para entidades públicas y privadas.

---

## 📜 3. Protocolos Operativos Estándar (SOPs en `protocols/`)

Los manuales de proceso paso a paso para el equipo humano:
- [`P01_correccion_pedagogica_bifasica.md`](protocols/P01_correccion_pedagogica_bifasica.md): El método de corrección que distingue a la Escuela.
- [`P02_solicitud_subvencion_publica.md`](protocols/P02_solicitud_subvencion_publica.md): Del triaje a la justificación final de ayudas públicas.
- [`P03_test_ab_oferta_formativa.md`](protocols/P03_test_ab_oferta_formativa.md): Cómo testar cursos con los alumnos sintéticos.
- [`P04_redaccion_autoral_antonia.md`](protocols/P04_redaccion_autoral_antonia.md): Criterios de creación en la voz de Antonia Molinero.
- [`P05_onboarding_nuevos_alumnos.md`](protocols/P05_onboarding_nuevos_alumnos.md): Acogida, entrevista de selección y matrícula.
- [`P06_creacion_y_supervision_carteleria.md`](protocols/P06_creacion_y_supervision_carteleria.md): Flujo de diseño gráfico y control de marca.

---

## 🎯 4. Principios Rectores y Reglas Inviolables

1. **Fuente Canónica Inmutable:** Toda la información sobre cursos, plazas, tarifas y profesores se valida contra [https://www.escuelaliteraria.com/](https://www.escuelaliteraria.com/).
2. **Estructura Bifásica Inviolable en la Crítica:** El análisis técnico interno descarnado y el comentario afectivo al alumno nunca se mezclan.
3. **Cero Clichés de Inteligencia Artificial:** Linter regex determinista (`evals/test_style_linter.py`) que bloquea automáticamente palabras artificiales (*"adéntrate", "tapiz", "crisol", "fascinante"*).
4. **Identidad Visual Corporativa:** Paleta editorial obligatoria (Fondo Marfil `#FAF8F5`, Tinta `#1A1A1A`, Terracota Canario `#C2593F`, Azul Atlántico `#1E3A5F`, Dorado `#D4A346`) y tipografías *Playfair Display* e *Inter*.

---

## 🧪 5. Verificación Continua de Calidad

Para comprobar la salud e integridad de toda la suite en cualquier momento:
```bash
python scripts/verify_installation.py
```
O para ejecutar la suite de evaluación con puntuación cuantitativa:
```bash
python evals/run_evals.py
```

---

## 🏛️ Créditos y Licencia

Desarrollado para la **Escuela Canaria de Creación Literaria S.L.** bajo la dirección pedagógica de **Antonia Molinero**.  
Todos los derechos reservados © 2004–2026. Ver archivo [`LICENSE`](LICENSE).

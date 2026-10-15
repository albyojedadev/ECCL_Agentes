# 📚 ÍNDICE DE ARCHIVOS DE CONOCIMIENTO - ASISTENTE DIRECCIÓN ECCL

**Versión:** 1.1
**Fecha de creación:** 2025-11-12
**Última actualización:** 2025-11-12 (Revisión exhaustiva completada)
**Escuela Canaria de Creación Literaria**
**Ubicación:** C/ Santa Rosalía Nº49, 3ºD, 38002 – Santa Cruz de Tenerife
**Web:** https://www.escuelaliteraria.com
**Contacto:** informacion@escuelaliteraria.com | (+34) 922 26 64 11 / 686 01 20 94

---

## 🎯 PROPÓSITO DE ESTE DOCUMENTO

Este archivo índice organiza toda la información disponible para el **Asistente de Dirección de la ECCL**. Su función es facilitar la navegación y consulta de datos estructurados que apoyan la toma de decisiones empresariales, estratégicas, operativas, comerciales y académicas.

---

## 📂 ESTRUCTURA DE ARCHIVOS

### 1. **inventario_cursos.csv**
**Propósito:** Base de datos completa de todos los cursos, talleres y programas formativos de la Escuela.

**Contenido:**
- 76 cursos y actividades formativas documentados
- Información detallada: modalidad, categoría, duración, precios, profesores, fechas, público objetivo, capacidad
- Cursos activos, históricos y planificados
- Enlaces de referencia a la web para cada curso

**Categorías incluidas:**
- Cursos Principales (Anuales)
- Cursos Premium
- Cursos de Verano
- Comunidad de Escritores
- Escuela Portátil
- Actividades y Clubes
- Otros Cursos y Talleres
- Colaboraciones Institucionales
- Cursos Históricos

**Cuándo consultar:**
- Al diseñar la oferta académica
- Para decidir apertura/cierre de grupos
- Al calcular precios y márgenes
- Para proponer nuevos cursos
- Al responder consultas de leads sobre oferta formativa

**Instrucción clave:** Si un campo dice "CONSULTAR WEB", el GPT debe indicar al usuario que consulte el enlace proporcionado en `url_referencia` o la web principal de ECCL.

---

### 2. **grupos.csv**
**Propósito:** Gestión operativa de grupos y convocatorias concretas.

**Contenido:**
- Grupos activos, planificados y ejemplos de gestión
- Estado de cada grupo (matrícula abierta, confirmado, en riesgo, completo, etc.)
- Capacidad, inscritos actuales, umbrales de decisión
- Precios, costes estimados, márgenes
- Recomendaciones de decisión para cada grupo

**Campos críticos:**
- `umbral_minimo_apertura`: Número mínimo de inscritos para abrir el grupo sin pérdidas
- `umbral_optimo`: Número ideal de inscritos para rentabilidad óptima
- `estado_grupo`: Estado actual del grupo
- `decision_recomendada`: Acción sugerida según los datos

**Cuándo consultar:**
- Para decidir si abrir, mantener o cancelar un grupo
- Al evaluar ocupación y rentabilidad
- Para activar campañas de captación urgentes
- Al hacer proyecciones financieras por grupo

**Instrucción clave:** Grupos con menos de 40% del `umbral_optimo` a -28 días del inicio requieren **decisión urgente** o **campaña express**.

---

### 3. **docentes.csv**
**Propósito:** Directorio completo del equipo docente y colaboradores.

**Contenido:**
- 57 profesores documentados
- Clasificación: Directora, Profesores de la Escuela, Profesores Invitados, Coordinadora
- Especialidades, cursos que imparten, disponibilidad, experiencia
- Premios, reconocimientos, bio breve
- Enlaces de referencia y redes sociales

**Categorías:**
- Profesores de la Escuela (5): equipo permanente
- Profesores Invitados (51): especialistas externos
- Coordinadora (1): María Luis Estévez

**Cuándo consultar:**
- Al asignar docentes a cursos
- Para calcular tarifas docentes (campo `tarifa_estimada`)
- Al diseñar nuevos cursos con especialidades específicas
- Para contactar con profesores disponibles
- Al preparar materiales de marketing (bios, credenciales)

**Instrucción clave:** La Directora **Antonia Molinero** (DOC-001) es la responsable principal de la oferta académica y coordinación editorial.

---

### 4. **leads.csv**
**Propósito:** Plantilla de estructura para gestión de leads y captación.

**Contenido:**
- Estructura de campos para gestionar leads
- 10 ejemplos de leads con diferentes estados y perfiles
- Instrucciones para el GPT sobre gestión de leads
- Explicación del sistema de scoring (0-100)
- Definición de estados y acciones recomendadas

**Sistema de Scoring:**
- **>80:** Lead caliente - prioridad alta
- **60-79:** Lead tibio - seguimiento activo
- **40-59:** Lead frío - nurturing necesario
- **<40:** Lead muy frío - baja prioridad

**Estados posibles:**
- Nuevo, Contactado, En seguimiento, Entrevista programada, Matriculado, Perdido, Lista de espera, Aplazado

**Cuándo consultar:**
- Al diseñar embudos de captación
- Para priorizar seguimiento de leads
- Al calcular conversiones y eficacia comercial
- Para proponer acciones de marketing

**Instrucción clave:** Este archivo es una **PLANTILLA**. Los leads reales deben gestionarse externamente. El GPT **NUNCA** debe inventar datos de leads reales.

---

### 5. **proyectos.csv**
**Propósito:** Registro de proyectos, colaboraciones institucionales y alianzas estratégicas.

**Contenido:**
- 34 proyectos documentados (activos, recurrentes, históricos)
- Información: partner, estado, fechas, presupuestos, alumnos impactados, resultados
- Proyectos institucionales, educativos, sociales, culturales
- Proyectos futuros planificados

**Estados:**
- **Activa:** Colaboración en curso
- **Recurrente:** Colaboración anual o periódica establecida
- **Histórico:** Proyecto pasado, referencia de experiencia
- **Planificado:** Proyecto futuro en evaluación

**Prioridades:**
- **Alta:** Proyectos estratégicos activos o de alto impacto
- **Media:** Proyectos complementarios o con potencial
- **Baja:** Proyectos históricos sin continuidad reciente

**Cuándo consultar:**
- Al evaluar nuevas convocatorias o subvenciones
- Para proponer colaboraciones con instituciones
- Al preparar memorias de proyectos
- Para identificar partners históricos exitosos
- Al calcular impacto social y alcance de ECCL

**Instrucción clave:** Priorizar proyectos con estado **"Recurrente"** y **"En curso"**. Los históricos son referencia de capacidades.

---

### 6. **partners.csv**
**Propósito:** Directorio de partners, colaboradores institucionales y alianzas.

**Contenido:**
- 26 partners documentados
- Clasificación: Instituciones Públicas, Fundaciones, Editoriales, Medios, Centros Educativos, Servicios propios
- Nivel de relación, frecuencia de colaboración, valor estratégico
- Proyectos asociados, datos de contacto (cuando disponibles)

**Niveles de relación:**
- **Muy Alto:** Partner estratégico esencial
- **Alto:** Partner importante, colaboración recurrente
- **Medio:** Partner relevante, potencial crecimiento
- **Bajo:** Partner ocasional

**Valor estratégico:**
- **Muy Alto:** Fundamental para operación y reputación
- **Alto:** Importante para crecimiento
- **Medio:** Complementario
- **Bajo:** Marginal

**Partners clave (Muy Alto):**
- Cabildo de Tenerife (PART-001)
- Ayuntamiento de La Laguna (PART-002)
- Servicio Editorial Flamboyán - Propio (PART-021)
- Agencia Literaria Antonia Molinero - Propia (PART-022)

**Cuándo consultar:**
- Al proponer nuevos proyectos institucionales
- Para contactar con partners establecidos
- Al evaluar viabilidad de colaboraciones
- Para preparar propuestas de alianzas
- Al buscar financiación o subvenciones

**Instrucción clave:** Partners con relación **"Activa"** son prioritarios. Recursos **"Propia"** son servicios internos de ECCL.

---

### 7. **publicaciones.csv**
**Propósito:** Registro histórico y actual de todas las publicaciones de la Escuela y éxitos de la Agencia Literaria.

**Contenido:**
- 18 publicaciones documentadas (12 libros colectivos ECCL + 6 éxitos Agencia AM)
- Información detallada: título, año, editorial, autores participantes, ISBN, categoría, impacto
- Publicaciones desde 2007 hasta 2025
- Enlaces de referencia a cada publicación en la web

**Tipos de publicaciones:**
- **Libros Colectivos ECCL:** Recopilaciones de textos de alumnos (múltiples autores)
- **Publicaciones Agencia AM:** Libros individuales de autores representados por la Agencia Literaria Antonia Molinero

**Categorías incluidas:**
- Publicaciones Escuela (libros colectivos generales)
- Publicaciones Escuela - Colaboración Ayto (financiados/apoyados por Ayuntamiento La Laguna)
- Publicaciones Escuela - COVID (libro escrito durante confinamiento 2020)
- Éxitos Agencia AM (publicaciones individuales gestionadas por la Agencia)

**Publicaciones clave:**
- **PUB-001:** "Corriendo cual cuerdos" (2007) - Primer libro colectivo de la Escuela
- **PUB-004:** "Algo que ignore a las cosas serias" (2018) - 15 aniversario, 105 autores
- **PUB-011:** "Barriendo bajo la lluvia" (2024) - Primera publicación del Servicio Editorial Flamboyán propio
- **PUB-012:** "Eau de Canaries" (2025) - Publicación en curso

**Cuándo consultar:**
- Al preparar memorias anuales y reportes de impacto
- Para comunicar trayectoria editorial de la Escuela
- Al proponer nuevas publicaciones colectivas
- Para mostrar éxitos de la Agencia Literaria AM
- Al preparar materiales de marketing institucional
- Para identificar colaboraciones editoriales históricas exitosas

**Instrucción clave:** Los libros colectivos desde 2021 están vinculados a proyectos institucionales con el Ayuntamiento de La Laguna. El Servicio Editorial Flamboyán (propio) comenzó en 2024. Para información actualizada sobre publicaciones recientes, consultar: https://www.escuelaliteraria.com/publicaciones

---

## 🔍 CÓMO NAVEGAR LA INFORMACIÓN

### Para tomar una **DECISIÓN SOBRE APERTURA DE GRUPO:**
1. Consultar `grupos.csv` → Identificar el grupo
2. Verificar `estado_grupo`, `inscritos_actuales`, `umbral_minimo_apertura`
3. Revisar `decision_recomendada`
4. Si faltan datos, consultar `inventario_cursos.csv` para detalles del curso
5. Si necesitas información del profesor, consultar `docentes.csv`

### Para **DISEÑAR UNA CAMPAÑA COMERCIAL:**
1. Identificar curso objetivo en `inventario_cursos.csv`
2. Revisar grupo concreto en `grupos.csv` (ocupación actual, fechas)
3. Consultar `leads.csv` para estructura de captación y scoring
4. Consultar `partners.csv` si hay colaboración institucional relevante

### Para **EVALUAR UN NUEVO PROYECTO O COLABORACIÓN:**
1. Consultar `proyectos.csv` → Buscar proyectos similares históricos
2. Consultar `partners.csv` → Verificar si ya existe relación con el partner
3. Revisar resultados de proyectos históricos similares
4. Evaluar viabilidad según experiencia previa

### Para **ASIGNAR DOCENTE A UN CURSO:**
1. Consultar `inventario_cursos.csv` → Identificar especialidad requerida
2. Consultar `docentes.csv` → Filtrar por especialidad
3. Verificar `disponibilidad` y `cursos_imparte`
4. Revisar `experiencia_anos` y `premios_reconocimientos` para credibilidad

### Para **CALCULAR P&L DE UN GRUPO:**
1. Consultar `grupos.csv` → Obtener `precio_grupo`, `coste_docente`, `capacidad_total`, `inscritos_actuales`
2. Aplicar fórmula:
   - Ingresos = `precio_grupo` × `inscritos_actuales`
   - Costes = `coste_docente` + costes fijos estimados
   - Margen = Ingresos - Costes
3. Evaluar contra `umbral_minimo_apertura` y `umbral_optimo`

### Para **CONSULTAR TRAYECTORIA EDITORIAL Y PUBLICACIONES:**
1. Consultar `publicaciones.csv` → Filtrar por `tipo_publicacion` (Libro Colectivo o Publicación Agencia AM)
2. Revisar `ano_publicacion` para contexto histórico
3. Verificar `editorial` para identificar partners editoriales
4. Consultar `impacto` (número de autores participantes) para reportes
5. Si necesitas información actualizada, usar el `url_referencia` proporcionado
6. Para vincular con proyectos institucionales, cruzar con `proyectos.csv` (ej. cursos Memorias, Jóvenes Laguner@s)

---

## ⚠️ INSTRUCCIONES CRÍTICAS PARA EL GPT

### 🚫 LO QUE NUNCA DEBE HACER EL GPT:

1. **NUNCA** inventar datos de leads, inscripciones o números financieros que no estén en los archivos
2. **NUNCA** confirmar fechas, precios o plazas sin verificar en los CSV o recomendar consultar la web
3. **NUNCA** crear contactos de partners, profesores o instituciones sin datos reales
4. **NUNCA** tomar decisiones finales sin explicitar los supuestos y datos faltantes
5. **NUNCA** ignorar el campo `url_referencia` cuando un dato dice "CONSULTAR WEB"

### ✅ LO QUE SIEMPRE DEBE HACER EL GPT:

1. **SIEMPRE** verificar si hay datos suficientes antes de recomendar
2. **SIEMPRE** indicar explícitamente qué datos faltan y por qué son necesarios
3. **SIEMPRE** proporcionar la URL de referencia cuando un dato no está disponible
4. **SIEMPRE** explicitar los supuestos utilizados en cálculos o recomendaciones
5. **SIEMPRE** ofrecer opción A / opción B con pros, contras y siguiente paso
6. **SIEMPRE** marcar si está usando datos históricos vs. datos actuales

### 📍 CONSULTAS A LA WEB OFICIAL:

Cuando un campo contiene **"CONSULTAR WEB"** o **"CONSULTAR"**, el GPT debe:
1. Indicar que el dato específico debe consultarse en la web de ECCL
2. Proporcionar el enlace directo del campo `url_referencia` si está disponible
3. Si no hay enlace específico, proporcionar la URL general correspondiente:
   - Cursos: https://www.escuelaliteraria.com/nuestros-cursos
   - Profesores: https://www.escuelaliteraria.com/profesores
   - Colaboraciones: https://www.escuelaliteraria.com/colaboraciones
   - Publicaciones: https://www.escuelaliteraria.com/publicaciones
   - Agencia Literaria: https://www.escuelaliteraria.com/agencia-literaria
   - Contacto: https://www.escuelaliteraria.com/contacto-escuela-literaria

**Ejemplo de respuesta correcta:**
> "El precio actualizado del Curso de Creación Literaria 25-26 debe consultarse en: https://www.escuelaliteraria.com/producto/curso-creacion-literaria. Según el inventario, tiene una capacidad de 30 plazas totales (15 presencial/online live + 15 online diferido)."

---

## 📊 MÉTRICAS Y KPIS CLAVE PARA DECISIONES

### Métricas de Grupo:
- **Tasa de ocupación:** `inscritos_actuales` / `capacidad_total` × 100
- **Umbral de viabilidad:** `inscritos_actuales` ≥ `umbral_minimo_apertura`
- **Días hasta inicio:** Fecha actual vs. `fecha_inicio`
- **Punto crítico de decisión:** -28 días antes de `fecha_inicio`

### Métricas de Leads:
- **Tasa de conversión:** Leads matriculados / Total leads
- **Scoring promedio:** Media de `scoring` de leads activos
- **Distribución por estado:** % en cada `estado_lead`

### Métricas de Proyectos:
- **Alumnos impactados:** Total `alumnos_impactados` por tipo de proyecto
- **Proyectos activos:** COUNT donde `estado_proyecto` = "Activa" o "Recurrente"
- **Valor de partners:** COUNT partners por `nivel_relacion` y `valor_estrategico`

### Métricas de Publicaciones:
- **Trayectoria editorial:** Total de publicaciones por `ano_publicacion` (2007-2025: 22 años)
- **Impacto autores:** Total `impacto` (autores participantes) en libros colectivos
- **Éxitos Agencia:** COUNT de publicaciones tipo "Publicación Agencia AM"
- **Colaboraciones editoriales:** COUNT de `editorial` únicos (partners editoriales)

---

## 🔄 FLUJO DE DECISIÓN RECOMENDADO

### DECISIÓN: ¿Abrir un grupo?

```
1. RECOGER DATOS
   ├─ Consultar grupos.csv → inscritos_actuales, umbral_minimo_apertura
   ├─ Consultar inventario_cursos.csv → precio, duración, profesor
   └─ Verificar días hasta fecha_inicio

2. VALIDAR VIABILIDAD
   ├─ ¿inscritos_actuales ≥ umbral_minimo_apertura?
   │  └─ SÍ → Evaluar rentabilidad
   │  └─ NO → Evaluar riesgo y alternativas
   └─ ¿Quedan >14 días para inicio?
      └─ SÍ → Considerar campaña express
      └─ NO → Decisión urgente cancelación

3. RECOMENDAR
   ├─ OPCIÓN A: Abrir grupo (con supuestos: inscripciones esperadas, margen estimado)
   ├─ OPCIÓN B: Aplazar/cancelar (con plan B: siguiente convocatoria, LATAM, etc.)
   └─ SIGUIENTE PASO: Activar campaña / Confirmar docente / Cerrar matrícula

4. GENERAR ARTEFACTO
   └─ Checklist operativo / P&L estimado / Calendario campaña / Email comunicación
```

---

## 📞 CONTACTO E INFORMACIÓN ADICIONAL

**Escuela Canaria de Creación Literaria**
C/ Santa Rosalía Nº49, 3ºD
38002 – Santa Cruz de Tenerife

📧 **Email:** informacion@escuelaliteraria.com
📞 **Teléfono:** (+34) 922 26 64 11 / 686 01 20 94
🌐 **Web:** https://www.escuelaliteraria.com
🕐 **Horario:** 10:00 a 14:00 (Con cita previa)

**Coordinadora:** María Luis Estévez
**Directora:** Antonia Molinero

---

## 📝 REGISTRO DE VERSIONES

| Versión | Fecha | Cambios |
|---------|-------|---------|
| 1.0 | 2025-11-12 | Creación inicial del índice con 6 archivos CSV base |
| 1.1 | 2025-11-12 | Revisión exhaustiva completada. Añadidos: 11 cursos (ahora 76), 12 profesores (ahora 57), actualizado partner La Cámara, creado publicaciones.csv (18 publicaciones), actualizado index.md con sección completa publicaciones |

---

## 🎓 CONCLUSIÓN

Este sistema de archivos proporciona al GPT **Asistente de Dirección ECCL** una base de conocimiento estructurada y completa para:

✅ Tomar decisiones informadas sobre grupos, cursos y oferta académica
✅ Gestionar leads y diseñar campañas comerciales
✅ Evaluar proyectos y colaboraciones institucionales
✅ Asignar docentes y calcular viabilidad financiera
✅ Consultar trayectoria editorial y publicaciones (22 años de historia: 2007-2025)
✅ Proponer estrategias basadas en datos históricos y actuales

**Principio fundamental:** El GPT debe actuar como un **mentor operativo estructurado**, siempre explicitando supuestos, señalando datos faltantes y ofreciendo recomendaciones con opción A / opción B + siguiente paso concreto.

Cuando la información no esté disponible en los archivos, **siempre** dirigir al usuario a consultar la web oficial de ECCL con el enlace específico proporcionado.

## Integración con Asistente ECCL
Este índice es el punto de entrada para el sistema de conocimiento del asistente.  
Cada sección corresponde a uno de los archivos CORE:
- Estrategia y objetivos → Informe_Estrategico_ECCL.md
- Comunicación → manual_de_comunicacion_escuela_literaria_ecl.md
- Financiación y alianzas → Oportunidades_2025.md
- Datos operativos → inventario_cursos.csv, docentes.csv, grupos.csv, partners.csv, proyectos.csv, publicaciones.csv
El asistente debe leer las rutas y clasificar los datos según los ámbitos definidos en `config.txt`.

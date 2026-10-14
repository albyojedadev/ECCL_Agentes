---
name: catalogo-academico-eccl
description: Consulta y validación canónica de cursos, tarifas, fechas, modalidades y claustro docente contra escuelaliteraria.com y los JSON canónicos.
---

# 📚 Skill: Catálogo Académico Canónico ECCL
### Consulta Factual de Cursos, Fechas y Profesores

## 🎯 1. Objetivo
Proveer información 100% veraz sobre la oferta docente, precios, modalidades y claustro de la Escuela sin margen de alucinación.

## 📥 2. Entradas Requeridas
- `termino_busqueda`: Nombre de curso, temática, fecha o profesor.

## ⚙️ 3. Procedimiento Paso a Paso
1. **Búsqueda en Base de Conocimiento:** Consultar `knowledge/catalogo/cursos_activos.json` y `claustro_docente.json`.
2. **Validación de Modalidad y Aforo:** Indicar si el curso es presencial (La Laguna), online live o diferido.
3. **Precios y Requisitos:** Detallar tarifas exactas y si exige muestra previa de escritura.

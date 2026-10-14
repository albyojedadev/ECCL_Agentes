---
name: synthetic-audience-panel-eccl
description: Invocación y simulación del panel de 18 avatares reales para test de estrés de nuevos cursos, precios, horarios y objeciones de compra.
---

# 👥 Skill: Panel de Audiencia Sintética ECCL
### Focus Group con los 18 Avatares Maestros

## 🎯 1. Objetivo
Simular la reacción de la comunidad estudiantil real ante cualquier propuesta formativa o comercial antes de su lanzamiento.

## 📥 2. Entradas Requeridas
- `propuesta`: Taller, precio, modalidad y fechas.
- `avatares_objetivo`: Lista de avatares a consultar o panel completo.

## ⚙️ 3. Procedimiento Paso a Paso
1. **Carga de Perfiles:** Consultar `knowledge/avatares/panel_18_alumnos.json`.
2. **Evaluación de Motivaciones vs Frenos:** Contrastar la propuesta con el tiempo, presupuesto y miedos de cada avatar seleccionado.
3. **Consolidación de Métricas:** Calcular porcentaje de aprobación y principales objeciones detectadas.

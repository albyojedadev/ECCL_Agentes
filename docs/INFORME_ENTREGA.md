# Informe de entrega y reevaluación

**Fecha de cierre:** 15 de octubre de 2026
**Versión:** 2.0.0
**Estado:** apta para entrega como repositorio corregido y para una prueba piloto controlada.

## Resultado frente al punto de partida

La auditoría inicial encontró pérdidas reales: el manual autoral estaba truncado, faltaban manuales y ejemplos de crítica, el panel sintético no incorporaba todas las fichas, varias capacidades históricas se habían reducido, siete filas de cursos estaban desplazadas y los controles automáticos aceptaban ejemplos inválidos.

La versión 2.0.0 corrige esos problemas y conserva el historial necesario para comprobarlo:

| Componente | Resultado final |
|---|---|
| Agentes, skills y protocolos | 17 agentes, 24 skills y 6 protocolos con procedimientos, decisiones, ejemplos y excepciones |
| Fuentes compradas | 99 entradas inventariadas; 98 archivos íntegros y un bloqueo temporal excluido con motivo |
| Voz autoral | Manual completo de 17.982 caracteres, siete variantes emocionales y corpus por género |
| Crítica | Dos manuales, módulo de siete ejes y 20 pares completos de informe/comentario |
| Panel | 18 avatares con procedencia y conflictos conservados |
| Corpus literario normalizado | 57 objetos completos; dos fragmentos truncados declarados, sin completar contenido inventado |
| Catálogo | 73 registros, 71 ID de curso distintos y 58 docentes con procedencia y vigencia no verificada |
| Evaluación | 32 regresiones y 26 trazas de comportamiento revisadas criterio por criterio |
| Instalación | Copia a destino, verificación del destino, carga de contexto y reconstrucción reproducible superadas |

## Correcciones de seguridad y honestidad

Los componentes distinguen hechos, históricos, propuestas y datos pendientes. El sistema no convierte un panel sintético en validación de mercado, una memoria en expediente presentado, una tipografía propuesta en norma institucional ni una guía en asesoramiento jurídico definitivo.

El crítico literario exige rol docente verificado o un servicio concreto habilitado. Si falta autorización, explica requisitos y deriva; no analiza el manuscrito. Los linters rechazan geometría ausente, márgenes negativos, desbordes, colores/fuentes no declarados y números no finitos.

## Evidencia incluida

- [Dictamen final](../auditoria/09_REEVALUACION_Y_DICTAMEN_FINAL.md)
- [Revisión adversarial independiente](../auditoria/reevaluacion/REVISION_ADVERSARIAL_FINAL.md)
- [Resultados de comportamiento](../evals/resultados/RESULTADOS_COMPORTAMIENTO.json)
- [Definición de los 26 casos](../evals/benchmark_dataset.json)
- [Instalación y carga](INSTALACION.md)
- [Procedencia del corpus](PROCEDENCIA.md)
- [Reglas comunes](REGLAS_COMUNES.md)

Los resultados incluyen respuestas generadas en sesiones de prueba, archivos cargados y revisión manual. Nueve respuestas de la versión anterior se conservan como baseline para comparaciones concretas.

## Límites que requieren al cliente

La entrega documental está cerrada, pero producción requiere la aceptación del cliente en su entorno: validar muestras de voz con Antonia Molinero, aprobar marca y políticas propuestas, ejecutar el piloto en una sesión autenticada y comprobar la vigencia de datos externos. Los casos E03 y E05 deben repetirse con antecedentes y filas reales autorizadas para probar la tarea completa, porque los inputs de auditoría solo permitían comprobar el rechazo prudente y el método.

Estas validaciones no representan pérdidas del traslado. Son la última capa de aceptación humana y operativa de un sistema que ya conserva las fuentes y documenta sus límites.

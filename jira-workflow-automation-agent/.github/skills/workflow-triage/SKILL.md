---
name: workflow-triage
description: Clasificar, priorizar y enrutar tickets según señales disponibles, explicando incertidumbre y siguiente acción. Use when GitHub Copilot needs this repeatable capability inside the corresponding engineering workflow.
---

# Workflow

1. Agrupar por tipo, urgencia e impacto.
2. Usar reglas explícitas del equipo cuando estén disponibles.
3. No cerrar ni escalar tickets automáticamente sin política autorizada.
4. Indicar por qué se propone cada prioridad o ruta.
5. Solicitar aprobación antes de acciones de escritura masivas.

# Guardrails

- Basar conclusiones en evidencia observable del repositorio, herramientas o fuentes autorizadas.
- No inventar estándares internos, APIs, IDs, aprobaciones ni resultados de pruebas.
- Minimizar privilegios y evitar secretos en prompts, logs, commits o archivos generados.
- Separar hechos, supuestos y recomendaciones.
- Antes de acciones irreversibles o de escritura externa, exigir confirmación cuando no esté explícitamente autorizada.

# Output

Entregar una respuesta breve y trazable con: objetivo, evidencia, análisis/acción, validación y riesgos pendientes.

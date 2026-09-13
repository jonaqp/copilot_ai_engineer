# Impact Radar — GitHub Copilot Agent

Agente predictivo de análisis de impacto para repositorios de software. Convierte el grafo de dependencias en un radar activo de riesgo arquitectónico.

## Qué incluye
- `.github/agents/impact-radar.agent.md`: agente principal.
- `.github/skills/`: cuatro skills especializadas.
- `references/`: estándar y modelo de riesgo.
- `scripts/`: herramientas deterministas para grafo, escaneo, impacto y gate.
- `demo_arch_radar/`: demo Python + Flask con una interfaz web.

## Capacidades
- Dependencias directas e indirectas.
- Detección de rutas de propagación.
- Priorización por criticidad.
- Score de riesgo 0-100.
- Recomendaciones de tests Shift-Left.
- Decisión GO / GO WITH CONDITIONS / NO-GO.

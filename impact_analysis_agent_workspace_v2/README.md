# Impact Radar — GitHub Copilot Agent

Agente predictivo de análisis de impacto para repositorios de software. Convierte el grafo de dependencias en un radar activo de riesgo arquitectónico.

## Qué incluye
- `.github/agents/impact-radar.agent.md`: agente principal.
- `.github/skills/`: cuatro skills especializadas.
- `references/`: estándar de impacto, modelo de riesgo y estándar del grafo visual.
- `scripts/`: herramientas deterministas para grafo, escaneo, impacto y gate.
- `demo_arch_radar/`: demo Python + Flask con una interfaz web y grafo interactivo.

## Capacidades
- Dependencias directas e indirectas.
- Detección de rutas de propagación.
- Priorización por criticidad.
- Score de riesgo 0-100.
- Recomendaciones de tests Shift-Left.
- Decisión GO / GO WITH CONDITIONS / NO-GO.
- Radar visual con pan/zoom, inspección de nodos y filtro de impacto.
- Dependencias ocultas resaltadas visualmente.

## Visualización
La demo usa **Cytoscape.js 3.34.x** desde CDN para renderizar el grafo en el navegador. No agrega dependencias Python nuevas. Si el CDN no está disponible, la pantalla muestra un fallback textual y el análisis funcional sigue operando.


## Regenerable static demo

`demo_arch_radar/static-demo.html` is intentionally delivered in BASE mode. The `graph-visualization-renderer` skill must overwrite it after each impact-analysis prompt by running `python scripts/regenerate_static_demo.py --component <id> --change-type <type>`. Visual improvements belong in the template/CSS/JS and are then preserved across future regenerations. See `USAGE_GUIDE.md`.

---
name: dependency-graph-builder
description: Construir o actualizar un grafo técnico de dependencias a partir de código, manifests, contratos, configuración y metadata de arquitectura. Usar cuando el agente necesite descubrir qué componentes dependen de otros, identificar conexiones directas e indirectas, o preparar un mapa base antes de un análisis de impacto.
---

# Purpose
Construir un grafo mínimo, verificable y útil para análisis de impacto.

# Inputs
- Archivos modificados o componente objetivo.
- Código, imports, llamadas, contratos, eventos y configuración.
- Metadata de arquitectura existente si está disponible.

# Workflow & Instructions
1. Buscar primero metadata explícita de arquitectura.
2. Complementar con evidencia del código solo cuando sea necesario.
3. Modelar cada componente como nodo estable.
4. Modelar una dependencia como `source depends_on target`.
5. Registrar tipo de dependencia y si está documentada.
6. Evitar duplicados y ciclos falsos.
7. Validar el grafo con `scripts/build_graph.py` si existe.

Para criterios de evidencia leer `.github/references/impact-analysis-standard.md` cuando haya ambigüedad.

# Expected Output
Entregar nodos, aristas, evidencia, dependencias dudosas y huecos de información.

# Validation
- Cada arista debe tener evidencia o marcarse como hipótesis.
- Los identificadores de componentes deben ser consistentes.
- No inferir llamadas remotas solo por similitud de nombres.

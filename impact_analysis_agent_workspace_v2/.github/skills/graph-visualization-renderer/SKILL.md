---
name: graph-visualization-renderer
description: Genera una visualizacion HTML real del grafo de dependencias y del impacto arquitectonico. Usar cuando el usuario pida ver el grafo, radar visual, mapa de dependencias, efecto domino o una vista HTML interactiva. Debe crear o actualizar HTML/CSS/JS ejecutable, no limitarse a tablas o descripciones textuales.
---

# Graph Visualization Renderer

## Purpose
Convertir el grafo tecnico y el resultado de impacto en una vista HTML visible, navegable y verificable.

## Inputs
- Grafo con `components` y `dependencies`.
- Reporte de impacto opcional con nodo raiz, profundidad y rutas.
- Plantilla HTML existente si la aplicacion ya tiene UI.

## Workflow
1. Leer el grafo real y el reporte de impacto; no inventar nodos ni aristas.
2. Crear un contenedor grafico dentro del HTML (`#impactGraph`).
3. Renderizar nodos y aristas con SVG + JavaScript local del proyecto.
4. Representar visualmente:
   - raiz del cambio;
   - impacto directo L1;
   - impacto indirecto L2+;
   - dependencias no documentadas con linea discontinua;
   - componentes no impactados atenuables.
5. Agregar inspector de nodo, leyenda y controles basicos.
6. Evitar dependencias CDN como requisito funcional; la demo debe funcionar offline tras instalar Python/Flask.
7. Validar que el HTML realmente incluya el contenedor y que el JavaScript cree un elemento `<svg>` con nodos y aristas.
8. Si el proyecto ya usa una libreria grafica local, puede reutilizarse; no introducir una nueva dependencia remota sin necesidad.

## Expected Output
Entregar archivos HTML/CSS/JS modificados y una ruta ejecutable que muestre el grafo. Una tabla de detalles puede complementar el grafo, pero nunca sustituirlo cuando esta skill se activa.

## Validation
- El HTML contiene `#impactGraph`.
- El payload serializado incluye componentes y dependencias.
- El JavaScript genera un SVG visible dentro de `#impactGraph`.
- Hay al menos un nodo por componente y una arista por dependencia disponible.
- El modo de impacto diferencia ROOT, L1 y L2+.
- No se requiere acceso a Internet para ver el grafo.

Consultar `references/visual-contract.md` para el contrato visual.

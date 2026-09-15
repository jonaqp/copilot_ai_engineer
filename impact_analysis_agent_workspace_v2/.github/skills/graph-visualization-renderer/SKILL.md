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
2. Tratar `demo_arch_radar/static-demo.html` como **artefacto regenerable**, no como fuente maestra.
   - Si no existe un escenario de impacto, ejecutar `scripts/regenerate_static_demo.py` sin `--component` para crear una demo BASE mínima.
   - Cada vez que un prompt solicite analizar un componente o tipo de cambio, ejecutar el script con `--component` y `--change-type`. El archivo DEBE sobrescribirse con el último escenario.
   - No acumular manualmente datos viejos dentro de `static-demo.html`; la fuente de verdad es `architecture.json` + el resultado actual del analizador.
3. Mantener la plantilla base en `demo_arch_radar/templates/static-demo.template.html`; las mejoras visuales permanentes deben hacerse en la plantilla, CSS o JS y luego regenerar el HTML.
4. Crear un contenedor grafico dentro del HTML (`#impactGraph`).
5. Renderizar nodos y aristas con SVG + JavaScript local del proyecto.
6. Representar visualmente:
   - raiz del cambio;
   - impacto directo L1;
   - impacto indirecto L2+;
   - dependencias no documentadas con linea discontinua;
   - componentes no impactados atenuables.
7. Agregar inspector de nodo, leyenda y controles basicos.
8. Evitar dependencias CDN como requisito funcional; la demo debe funcionar offline tras instalar Python/Flask.
9. Validar que el HTML realmente incluya el contenedor y que el JavaScript cree un elemento `<svg>` con nodos y aristas.
10. Si el proyecto ya usa una libreria grafica local, puede reutilizarse; no introducir una nueva dependencia remota sin necesidad.
11. Tras cada regeneracion, validar que `static-demo.html` refleja el ROOT, L1/L2+, riesgo y decision del escenario actual.

### Comandos deterministas
Demo base:
```bash
python .github/skills/graph-visualization-renderer/scripts/regenerate_static_demo.py
```

Actualizar por prompt:
```bash
python .github/skills/graph-visualization-renderer/scripts/regenerate_static_demo.py --component pricing-service --change-type contract
```

También existe el wrapper corto:
```bash
python scripts/regenerate_static_demo.py --component pricing-service --change-type contract
```

## Expected Output
Entregar archivos HTML/CSS/JS modificados y una ruta ejecutable que muestre el grafo. `static-demo.html` debe quedar sobrescrito con la version correspondiente al ultimo prompt ejecutado. Una tabla de detalles puede complementar el grafo, pero nunca sustituirlo cuando esta skill se activa.

## Validation
- El HTML contiene `#impactGraph`.
- El payload serializado incluye componentes y dependencias.
- El JavaScript genera un SVG visible dentro de `#impactGraph`.
- Hay al menos un nodo por componente y una arista por dependencia disponible.
- El modo de impacto diferencia ROOT, L1 y L2+.
- No se requiere acceso a Internet para ver el grafo.
- El modo BASE contiene `impactData = null`.
- El modo ANALYSIS contiene el componente raiz y el escenario actual, sin residuos del escenario anterior.

Consultar `references/visual-contract.md` para el contrato visual.

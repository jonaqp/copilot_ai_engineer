# Guía de uso

## 1. Instalar la demo

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
```

## 2. Ejecutar la aplicación web

```bash
python demo_arch_radar/app.py
```

Abrir `http://127.0.0.1:5000`.

La pantalla incluye ahora un **Radar visual de impacto** construido con Cytoscape.js:
- rojo: componente modificado;
- amarillo: impacto directo (L1);
- cyan: impacto indirecto (L2+);
- gris: resto del ecosistema;
- línea roja discontinua: dependencia oculta/no documentada.

Puedes hacer zoom, mover el grafo, seleccionar nodos, centrarlo y activar `Solo impacto` para aislar el efecto dominó.

> La librería Cytoscape.js se carga desde CDN en esta demo. El motor Python y los análisis CLI no dependen de conexión externa.

## 3. Ejecutar análisis por CLI

```bash
python scripts/analyze_impact.py \\
  --graph demo_arch_radar/sample_system/architecture.json \\
  --component pricing-service \\
  --change-type contract
```

Prueba también:

```bash
python scripts/analyze_impact.py --graph demo_arch_radar/sample_system/architecture.json --component order-db --change-type schema
```

## 4. Ejecutar el gate preventivo

```bash
python scripts/quality_gate.py \\
  --graph demo_arch_radar/sample_system/architecture.json \\
  --component order-db \\
  --change-type schema \\
  --tested checkout-api notification-service analytics-consumer
```

El script devuelve código distinto de cero si el cambio queda en NO-GO.

## 5. Usar el agente en GitHub Copilot

Selecciona `impact-radar` y prueba:

> Analiza el impacto de cambiar la respuesta de `pricing-service`. Construye el mapa de dependencias, identifica efecto dominó, puntúa el riesgo y dime qué tests debo ejecutar antes del deploy. No modifiques código todavía.

Para pedir el radar visual:

> Analiza el cambio de `pricing-service` y actualiza la vista Impact Radar para mostrar visualmente el nodo raíz, impactos L1/L2+, dependencias ocultas y el gate recomendado. Mantén el grafo como una proyección de evidencias del repositorio.

Para un cambio real:

> Revisa el diff actual. Identifica las class y def modificadas, mapea qué componentes dependen de ellas directa o indirectamente y entrega GO / GO WITH CONDITIONS / NO-GO con evidencias.

## Grafo visual corregido

La visualizacion ya no depende de un CDN. El grafo se genera como SVG desde `demo_arch_radar/static/impact-graph.js` y aparece dentro de `#impactGraph`.

### Prueba inmediata sin Flask

Abre directamente:

`demo_arch_radar/static-demo.html`

Debe mostrar el ecosistema completo, el nodo raiz en rojo, impactos L1 en amarillo, L2+ en cyan y dependencias ocultas con linea roja discontinua.

### Prompt recomendado para el agente

```text
Analiza el impacto de cambiar el contrato de pricing-service y genera una visualizacion HTML del grafo de la aplicacion. Usa graph-visualization-renderer. Quiero ver nodos, aristas, ROOT, L1, L2+, dependencias ocultas e inspector de componentes. No reemplaces el grafo por una tabla.
```

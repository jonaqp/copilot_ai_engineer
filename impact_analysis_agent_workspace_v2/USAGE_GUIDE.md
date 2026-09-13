# Guía de uso — Impact Radar regenerable

## 1. Concepto de la demo

`demo_arch_radar/static-demo.html` ya no es una maqueta fija. Es un **artefacto regenerable** que el agente debe reemplazar con el escenario del último prompt.

La versión incluida en el ZIP se entrega en modo **BASE**:
- muestra el mapa técnico real;
- muestra nodos, aristas, owners y criticidad;
- no trae un ROOT ni riesgo preseleccionado;
- sirve como punto de partida mínimo para comprobar que el grafo funciona.

## 2. Probar la demo base sin Flask

Desde la raíz del workspace:

```bash
python scripts/regenerate_static_demo.py
python scripts/validate_graph_ui.py demo_arch_radar/static-demo.html
```

Luego abre:

`demo_arch_radar/static-demo.html`

Debe verse el grafo completo en modo neutro.

## 3. Simular lo que hará el agente después de un prompt

Ejemplo:

```bash
python scripts/regenerate_static_demo.py \
  --component pricing-service \
  --change-type contract

python scripts/validate_graph_ui.py demo_arch_radar/static-demo.html
```

El mismo `static-demo.html` queda **sobrescrito**. Al recargarlo en el navegador debe mostrar:
- `pricing-service` como ROOT;
- impactos directos L1;
- impactos indirectos L2+;
- dependencias ocultas;
- risk score;
- decisión GO / GO WITH CONDITIONS / NO-GO;
- validaciones Shift-Left.

Puedes cambiar de escenario sin crear archivos nuevos:

```bash
python scripts/regenerate_static_demo.py \
  --component order-db \
  --change-type schema
```

Al volver a abrir o recargar `static-demo.html`, el radar debe reflejar **solo el nuevo escenario**.

## 4. Ciclo esperado en GitHub Copilot

Selecciona el agente `impact-radar` y usa prompts como:

> Analiza el impacto de cambiar el contrato de `pricing-service`. Actualiza `static-demo.html` para que el grafo refleje ROOT, L1, L2+, dependencias ocultas, riesgo y gate. Valida el HTML generado antes de terminar.

El agente debe seguir:

```text
Prompt
  ↓
Analizar cambio
  ↓
Actualizar grafo / impacto
  ↓
Regenerar static-demo.html
  ↓
Validar HTML
  ↓
Abrir o recargar el mismo archivo
```

## 5. Mejorar progresivamente el radar

Si el prompt pide una mejora visual permanente —por ejemplo filtros por owner, agrupación por dominio, etiquetas de criticidad o una nueva leyenda— el agente debe:

1. modificar `demo_arch_radar/templates/static-demo.template.html`, `static/styles.css` o `static/impact-graph.js`;
2. volver a ejecutar `scripts/regenerate_static_demo.py` con el escenario actual;
3. validar el HTML;
4. conservar esas mejoras para los siguientes análisis.

Así el HTML se actualiza con cada análisis, mientras el renderer evoluciona gradualmente con los prompts.

## 6. Ejecutar la aplicación Flask

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python demo_arch_radar/app.py
```

Abrir `http://127.0.0.1:5000`.

El grafo SVG usa JavaScript local y no depende de CDN.

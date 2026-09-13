# Prompts de ejemplo para Impact Radar

## Caso 1 — contrato API
Analiza el impacto de cambiar el contrato de `pricing-service`. Identifica dependientes directos e indirectos, conexiones ocultas, score de riesgo y tests Shift-Left. No modifiques código.

## Caso 2 — esquema de base de datos
Voy a cambiar el esquema de `order-db`. Evalúa el efecto dominó sobre APIs y consumidores asíncronos. Entrega rutas de propagación y decisión GO / GO WITH CONDITIONS / NO-GO.

## Caso 3 — diff real
Revisa el diff actual. Detecta las `class`, `def`, endpoints o contratos modificados. Construye/actualiza el grafo solo con evidencia del repo y genera el análisis de impacto antes de proponer cambios.

## Caso 4 — preparación de pruebas
Para el cambio actual, no implementes todavía. Dime primero qué pruebas de contrato, integración, funcionales y regresión son necesarias para cubrir todas las rutas de impacto de criticidad alta.

# Estándar de visualización — Impact Radar

## Objetivo
Convertir el análisis de impacto en un grafo operativo que permita entender la propagación del cambio sin leer primero tablas extensas.

## Convenciones visuales
- **Nodo raíz**: componente modificado. Debe ser el foco visual principal.
- **Impacto directo (L1)**: dependiente inmediato del nodo raíz.
- **Impacto indirecto (L2+)**: dependiente transitivo.
- **No impactado**: permanece visible en vista ecosistema, pero con menor protagonismo.
- **Dependencia oculta/no documentada**: arista discontinua y destacada como riesgo.
- Mostrar siempre dirección de las aristas y el tipo de acoplamiento (`sync-api`, `async-event`, `database`, etc.).

## Interacción mínima
- Pan y zoom.
- `Fit/Centrar` para recuperar la vista completa.
- Toggle `Solo impacto` para atenuar componentes fuera del efecto dominó.
- Click en nodo para abrir criticidad, owner, profundidad y validación recomendada.

## Regla de evidencia
El grafo visual no debe inventar relaciones. Cada arista debe provenir del grafo técnico o quedar explícitamente marcada como hipótesis en implementaciones futuras.

## Tecnología demo
La demo usa **Cytoscape.js** para visualización interactiva. El cálculo de impacto sigue en Python; el navegador recibe únicamente JSON serializable del grafo y del reporte.

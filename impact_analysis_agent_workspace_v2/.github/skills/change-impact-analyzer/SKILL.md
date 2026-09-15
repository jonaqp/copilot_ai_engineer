---
name: change-impact-analyzer
description: Analizar el efecto dominó de un cambio recorriendo dependientes directos y transitivos de un componente, API, servicio, módulo, clase o función. Usar cuando se necesite responder qué se puede romper o degradar, mostrar rutas de propagación y separar impacto confirmado de impacto potencial.
---

# Purpose
Convertir un cambio localizado en un mapa de impacto trazable.

# Inputs
- Componente/símbolo cambiado.
- Tipo de cambio.
- Grafo de dependencias.

# Workflow & Instructions
1. Identificar el nodo raíz.
2. Recorrer dependientes inversos por profundidad.
3. Registrar ruta completa desde cada dependiente al nodo cambiado.
4. Marcar nivel 1 como impacto directo y nivel 2+ como indirecto.
5. Aumentar atención sobre dependencias no documentadas.
6. Asociar una validación concreta a cada ruta relevante.
7. Detenerse cuando no existan nuevos nodos o se alcance el límite solicitado.

# Expected Output
Tabla con componente, nivel, ruta, tipo de dependencia, criticidad, evidencia y validación.

# Validation
Toda fila debe ser reproducible a partir del grafo. No reportar nodos desconectados.

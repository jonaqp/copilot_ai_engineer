---
name: risk-predictor
description: Calcular y explicar un score de riesgo arquitectónico para cambios de contrato, esquema, comportamiento, configuración, dependencia o rendimiento. Usar después de identificar el alcance del cambio para clasificar Bajo, Medio, Alto o Crítico y justificar la predicción con factores observables.
---

# Purpose
Priorizar cambios según probabilidad, alcance e impacto.

# Inputs
- Tipo de cambio.
- Criticidad del componente raíz.
- Dependientes alcanzados y profundidad.
- Dependencias ocultas/no documentadas.
- Evidencia de tests.

# Workflow & Instructions
1. Cargar `../../../references/risk-model.md`.
2. Usar la severidad base del tipo de cambio.
3. Añadir peso por criticidad, alcance, profundidad y conexiones ocultas.
4. Aplicar mitigación solo por evidencias concretas de pruebas.
5. Limitar score a 0-100.
6. Explicar los factores que más contribuyen.

# Expected Output
Entregar `score`, `level`, factores, mitigaciones y confianza.

# Validation
El mismo conjunto de entradas debe producir la misma clasificación. No reducir riesgo por una prueba que no cubra la ruta afectada.

# Modelo de riesgo arquitectónico

## Escala
El score es 0-100.

- 0-24: Bajo
- 25-49: Medio
- 50-74: Alto
- 75-100: Crítico

## Factores
- Severidad base del tipo de cambio.
- Criticidad del componente objetivo.
- Cantidad de dependientes alcanzados.
- Profundidad máxima de propagación.
- Dependencias ocultas/no documentadas.
- Falta de pruebas relevantes.

## Severidad base sugerida
- `behavior`: 15
- `performance`: 20
- `config`: 25
- `dependency`: 30
- `contract`: 40
- `schema`: 45

## Política de gate
- Bajo/Medio: puede continuar con validaciones definidas.
- Alto: GO WITH CONDITIONS; exigir evidencias de pruebas sobre rutas críticas.
- Crítico: NO-GO por defecto hasta mitigar o aprobar explícitamente.

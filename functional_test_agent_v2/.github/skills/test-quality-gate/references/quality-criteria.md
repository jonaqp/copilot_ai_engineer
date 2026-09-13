# Criterios de calidad de tests

## Bloqueantes
- Test fallido.
- Coverage global <80%.
- `assert True` o equivalente trivial.
- Test dependiente de red real.
- Estado compartido no restaurado entre tests.

## Advertencias
- Mock excesivo.
- Test con demasiados comportamientos.
- Fixture demasiado opaca.
- Módulo crítico <70% aunque el global pase.

# Estándar de Testing Python

## Objetivo
Mantener una suite rápida, legible y orientada a comportamiento. El coverage es una señal de huecos, no el objetivo único.

## Convenciones
- Framework: `pytest`.
- Nombres: `test_<comportamiento>_<resultado>()`.
- Estructura: Arrange -> Act -> Assert.
- Fixtures en `tests/conftest.py` para setup compartido.
- Parametrizar datos equivalentes o bordes.
- Usar `pytest.raises` para excepciones esperadas.
- Evitar mocks de clases internas cuando puede probarse el flujo real en memoria.

## Clases y métodos
Para cada clase relevante revisar:
1. Constructor y estado inicial.
2. Métodos públicos.
3. Transiciones de estado.
4. Validaciones y excepciones.
5. Casos vacíos, cero, máximos y elementos inexistentes.

## Funciones
Para cada función pública revisar:
1. Entrada normal.
2. Entrada inválida.
3. Bordes.
4. Efectos secundarios.
5. Excepciones y ramas.

## Cobertura
- Global obligatorio: >=80%.
- Recomendado: >=90% para módulos de negocio.
- No excluir líneas para maquillar resultados.
- Revisar branch coverage cuando exista lógica condicional.

---
name: functional-test-authoring
description: Crear o mejorar tests pytest para clases, funciones y reglas de negocio Python. Usar cuando haya métodos, funciones públicas, validaciones, ramas, estados o errores sin cobertura suficiente y se necesiten pruebas funcionales o de lógica orientadas a comportamiento.
---

# Functional Test Authoring

## Purpose
Probar comportamiento real de clases y funciones con casos felices, inválidos y límite.

## Inputs
- Módulo Python bajo prueba.
- Tests existentes relacionados.
- `reference-standards/testing-standard.md`.
- Coverage actual si está disponible.

## Workflow & Instructions
1. Enumerar API pública: clases, métodos y funciones relevantes.
2. Identificar entradas, salidas, efectos de estado, excepciones y ramas.
3. Elegir primero comportamientos de mayor riesgo.
4. Crear tests con Arrange -> Act -> Assert.
5. Usar `pytest.mark.parametrize` para matrices de entradas.
6. Para clases con estado, probar transiciones válidas e inválidas.
7. Para errores esperados, usar `pytest.raises` con mensaje cuando aporte valor.
8. No probar getters triviales salvo que transformen o validen datos.
9. Ejecutar tests focalizados y luego coverage completo.

## Expected Output
Tests legibles que eleven cobertura útil del módulo sin acoplarse innecesariamente a detalles internos.

## Validation
- Todos los tests pasan.
- Cero asserts triviales.
- Casos críticos cubiertos.
- Coverage global >=80% al finalizar.

# Functional Testing Repository Instructions

Estas instrucciones aplican a toda tarea de testing Python/Flask del repositorio.

## Objetivo
Crear pruebas funcionales y de lógica que aumenten la confianza del software y mantengan coverage total >=80%, sin optimizar de forma ciega por porcentaje.

## Flujo obligatorio
1. Diagnosticar el comportamiento solicitado y ubicar código + tests relacionados.
2. Leer solo las referencias necesarias en `reference-standards/`.
3. Seleccionar la skill pertinente en `.github/skills/`.
4. Medir el baseline con `pytest --cov` o `python scripts/run_quality_gate.py`.
5. Priorizar huecos de alto riesgo: reglas de negocio, ramas, errores, rutas y clases con estado.
6. Implementar tests claros con Arrange -> Act -> Assert.
7. Ejecutar tests focalizados primero y luego la suite completa.
8. Corregir solo lo que falle; máximo 2 reintentos por el mismo criterio.
9. Finalizar con evidencia: coverage, tests ejecutados y riesgos restantes.

## Estándares de test
- Framework principal: `pytest`.
- Para Flask, usar `app.test_client()` y `app.app_context()`.
- Preferir comportamiento público antes que métodos privados.
- Un test debe fallar por una sola razón comprensible.
- Evitar sleeps, red real, reloj real no controlado y aleatoriedad sin semilla.
- Para clases con estado, probar transiciones y límites.
- Para funciones puras, usar parametrización y bordes.
- Para endpoints, probar status code, payload/HTML observable y cambios de estado.
- Para errores esperados, afirmar tipo de error o respuesta específica.
- Reutilizar fixtures para setup repetido, sin ocultar la intención del test.

## Coverage
- Umbral mínimo global: 80%.
- Objetivo recomendado del demo: >=90%.
- No excluir código útil solo para subir coverage.
- Priorizar branch coverage cuando exista lógica condicional relevante.
- Un archivo crítico por debajo de 70% debe revisarse aunque el global supere 80%.

## Selección de skills
- Clases, funciones y reglas de negocio: `.github/skills/functional-test-authoring/SKILL.md`.
- Rutas Flask y flujos web: `.github/skills/flask-functional-testing/SKILL.md`.
- Diagnóstico de huecos: `.github/skills/coverage-gap-analyzer/SKILL.md`.
- Validación final: `.github/skills/test-quality-gate/SKILL.md`.

## Guardrails
- No modificar producción para satisfacer un test mal diseñado.
- No esconder fallos con `try/except` en tests.
- No usar asserts triviales como `assert True`.
- No abusar de mocks; mockear fronteras externas, no lógica interna.
- No tocar archivos fuera del alcance sin justificarlo.

## Salida esperada
- comportamiento cubierto;
- tests creados/modificados;
- comando de validación;
- coverage final;
- huecos o riesgos que permanecen.

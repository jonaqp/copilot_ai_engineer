# Diseño del agente

El agente sigue seis bloques: Role & Goal, Context & Knowledge, Instructions & Planning, Tools & Skills, Guardrails & Permissions, Validation & Feedback.

## Skills
- `functional-test-authoring`: clases, funciones y reglas.
- `flask-functional-testing`: rutas y flujos Flask.
- `coverage-gap-analyzer`: priorización según coverage.
- `test-quality-gate`: validación final determinista.

## Principios
- Contexto progresivo: leer solo código y referencias relevantes.
- Trigger preciso: cada skill tiene un alcance distinto.
- Scripts deterministas: coverage y quality gate se ejecutan con scripts.
- Tool minimization: read/search/edit/execute.
- Validation loop: corregir solo criterios que fallen, máximo dos ciclos.

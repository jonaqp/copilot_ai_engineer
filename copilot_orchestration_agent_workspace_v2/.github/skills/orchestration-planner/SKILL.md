---
name: orchestration-planner
description: Construye un DAG de ejecución para tareas complejas de software. Usar cuando el trabajo deba descomponerse entre subagentes, detectar dependencias, separar tareas paralelas de secuenciales y definir criterios de fan-in antes de ejecutar.
---


# Orchestration Planner
## Purpose
Transformar una solicitud en un plan ejecutable y verificable.
## Workflow
1. Extraer objetivo, restricciones y aceptación.
2. Crear workstreams con `id`, `agent`, `inputs`, `outputs`, `depends_on`, `critical`.
3. Agrupar como `parallel_wave` solo tareas sin dependencia de escritura entre sí.
4. Definir fan-in y condición de salida.
5. Guardar el plan en `demo_orchestration/run/plan.json` cuando se use la demo.
## Expected Output
DAG pequeño, explícito y sin ciclos.
## Validation
Todo workstream obligatorio tiene owner; ninguna tarea corre antes de sus dependencias; el gate final depende de evidencias.
Leer `references/plan-contract.md` cuando se necesite el schema.

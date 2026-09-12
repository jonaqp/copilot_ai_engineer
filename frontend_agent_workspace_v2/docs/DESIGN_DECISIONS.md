# Decisiones de diseño del agente

## Estructura del agente
La configuración separa explícitamente:
- Role & Goal
- Context & Knowledge
- Instructions & Planning
- Tools & Skills
- Guardrails & Permissions
- Validation & Feedback

## Skills
Cada skill tiene propósito y trigger claros, inputs, workflow, expected output y validation. Se evita solapamiento: la skill general de componentes excluye tablas y la tabla tiene su propia skill.

## Optimización de contexto
El agente carga referencias solo cuando son relevantes. La documentación extensa vive fuera del prompt principal y los checks repetitivos se ejecutan con scripts.

## Seguridad y gobierno
El perfil limita herramientas a lectura, búsqueda, edición y ejecución local. No habilita web ni integraciones externas por defecto. Los cambios críticos o fuera de alcance deben requerir aprobación explícita.

## Validación
El ciclo es acotado: validar, corregir el criterio concreto y revalidar; máximo dos ciclos automáticos por el mismo error.

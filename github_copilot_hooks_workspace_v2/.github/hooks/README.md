# Hooks de la demo

Esta carpeta esta ordenada para que la demo sea facil de explicar.

## 1. hooks-explicador.json
Es el mapa de eventos. Indica **cuando** debe ejecutarse cada hook y que script llamar.

## 2. scripts/hook_explicador.py
Es la logica de los hooks. Recibe JSON por `stdin`, registra el evento y devuelve una respuesta cuando corresponde.

## 3. logs/hook-trace.jsonl
Es la evidencia. Cada linea representa un evento observado.

## Hooks usados

| Hook | Cuando ocurre | Para que sirve en esta demo |
|---|---|---|
| `sessionStart` | Al iniciar o reanudar una sesion | Registrar el inicio y explicar que la sesion comenzo |
| `userPromptSubmitted` | Cuando el usuario envia un prompt | Registrar que llego una solicitud |
| `preToolUse` | Antes de una tool | Permitir la accion demo y bloquear ejemplos peligrosos |
| `postToolUse` | Despues de una tool exitosa | Registrar que la tool termino bien |
| `postToolUseFailure` | Si la tool falla | Registrar el error y recomendar revisar antes de reintentar |
| `agentStop` | Cuando el agente intenta terminar | Confirmar que puede finalizar |
| `sessionEnd` | Al cerrar la sesion | Registrar el cierre |

La demo no usa MCP, Skills ni servicios externos.

# Prompts de prueba

## A. Explicar todos los hooks

> Usa hooks-governance-lab. Recorre HOOK_CATALOG.md y explicame que problema resuelve cada hook usando ejemplos de este repositorio. No cambies codigo.

## B. Demostrar preToolUse

> Simula una herramienta segura y una destructiva. Muestrame el payload de entrada, la salida del hook y explica por que una queda ALLOW y la otra DENY.

## C. Demostrar postToolUse

> Modifica Calculator agregando un metodo square con su test. Despues explicame que aporta postToolUse y ejecuta el quality gate.

## D. Demostrar agentStop

> Rompe temporalmente un test, simula agentStop y demuestra que el hook obliga al agente a continuar. Luego restaura el test y demuestra que permite finalizar.

## E. Demostrar subagentes

> Delega una revision pequena a un subagente y explicame que informacion pueden observar subagentStart y subagentStop.

## F. Auditoria completa

> Ejecuta scripts/simulate_hooks.py --all y resume audit.jsonl por evento, resultado y finalidad.

## G. Explicar la diferencia entre agente y hook

> Explica con esta demo la diferencia entre lo que decide el agente y lo que impone un hook. Incluye un ejemplo de seguridad y otro de quality gate.

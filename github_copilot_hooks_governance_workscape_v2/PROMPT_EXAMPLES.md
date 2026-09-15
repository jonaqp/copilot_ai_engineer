# Prompts de prueba

## A. Explicar hooks

> Usa hooks-governance-lab. Recorre HOOK_CATALOG.md y explícame qué problema resuelve cada hook usando ejemplos de este repositorio. No cambies código.

## B. Demostrar preToolUse

> Simula una tool segura y una destructiva. Enséñame el payload de entrada, la salida del hook y por qué una queda ALLOW y la otra DENY.

## C. Demostrar postToolUse

> Modifica Calculator agregando un método square con su test. Después explícame qué aporta postToolUse y ejecuta el quality gate.

## D. Demostrar agentStop

> Rompe temporalmente un test, simula agentStop y demuestra que el hook fuerza continuación. Después restaura el test y demuestra que permite finalizar.

## E. Demostrar subagentes

> Delega una revisión pequeña a un subagente y explícame qué información pueden observar subagentStart y subagentStop.

## F. Auditoría completa

> Ejecuta scripts/simulate_hooks.py --all y resume el audit.jsonl por evento, resultado y finalidad.

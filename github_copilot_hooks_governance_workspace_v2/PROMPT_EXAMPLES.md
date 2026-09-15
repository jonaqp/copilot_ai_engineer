# Prompts para probar el laboratorio

## Comprender preToolUse

> Usa hooks-governance-lab. Antes de modificar el carrito, explica que recibe `preToolUse`. Simula un comando seguro para ejecutar tests y otro destructivo. No evadas la decision del hook.

## Cambio funcional con quality gate

> Agrega un metodo para vaciar el carrito. Crea sus tests. Explica que hooks participan desde mi prompt hasta `agentStop`. No finalices si la suite de `demo_cart` falla.

## Demostrar postToolUse

> Modifica una regla de descuento del carrito y demuestra como `postToolUse` agrega contexto para recordar ejecutar pruebas focalizadas.

## Demostrar agentStop

> Rompe temporalmente un test del carrito, ejecuta el hook `agentStop`, muestra el BLOCK, corrige el test y vuelve a ejecutar hasta obtener ALLOW.

## Auditoria

> Ejecuta un escenario del carrito y despues resume las ultimas entradas de `.github/hooks/logs/audit.jsonl` indicando evento, outcome y razon.

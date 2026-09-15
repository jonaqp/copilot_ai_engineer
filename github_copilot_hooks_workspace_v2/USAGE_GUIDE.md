# Guia de uso

## Objetivo
Enviar cualquier prompt y observar, en orden, que hook participa y para que sirve.

## Opcion A - Demo local determinista

```bash
python scripts/simular_prompt.py "crea una funcion suma"
```
Veras una secuencia como:

```text
sessionStart
userPromptSubmitted
preToolUse
TOOL
postToolUse
agentStop
sessionEnd
```

Despues:

```bash
python scripts/ver_traza.py
```

## Opcion B - Copilot CLI
Usa este repositorio con Copilot CLI. Los hooks de repositorio se cargan desde `.github/hooks/*.json`.
Selecciona el agente `hooks-explicador` y envia cualquier prompt sencillo.
El agente ejecutara `python demo/accion_demo.py` una vez para provocar `preToolUse` y `postToolUse`.

## Importante
No todos los hooks se disparan en cada interaccion real:
- `sessionStart` depende del inicio/reanudacion de sesion.
- `preToolUse` y `postToolUse` requieren que se use una tool.
- `postToolUseFailure` solo aparece cuando una tool falla.
- `sessionEnd` aparece al terminar la sesion, no necesariamente al terminar una sola respuesta.

Por eso `scripts/simular_prompt.py` existe: permite explicar todo el ciclo en una sola ejecucion controlada.

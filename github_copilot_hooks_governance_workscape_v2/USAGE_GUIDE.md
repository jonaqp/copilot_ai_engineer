# Guía de uso

## 1. Baseline

```bash
python scripts/validate_workspace.py
```

Debe terminar con `RESULT: PASS`.

## 2. Ver todos los hooks sin Copilot

```bash
python scripts/simulate_hooks.py --all
```

Esto alimenta payloads de ejemplo al mismo `hook_handler.py` usado por los hooks del repositorio.

## 3. Probar la política más importante

```bash
python scripts/run_demo_scenarios.py
```

Esperado:

```text
SAFE TOOL      : allow
DANGEROUS TOOL : deny
SECRET TOOL    : deny
AGENT STOP     : allow
RESULT         : PASS
```

## 4. Probar el agente

Selecciona `hooks-governance-lab` y usa uno de los prompts de `PROMPT_EXAMPLES.md`.

## 5. Qué observar

- El agente explica el objetivo.
- `preToolUse` toma decisiones deterministas.
- `postToolUse` añade guía después de cambios.
- `agentStop` ejecuta tests y puede bloquear la finalización.
- Los eventos quedan trazados en `.github/hooks/logs/audit.jsonl`.

## 6. Demo de fallo del quality gate

Cambia temporalmente una expectativa de `demo_app/test_calculator.py` y ejecuta:

```bash
python scripts/simulate_hooks.py --event agentStop
```

Debe devolver `decision: block`. Restaura el test y repite; debe devolver `allow`.

## 7. Sobre `session-prompt-demo.json`

Viene con `disableAllHooks: true` para que no auto-inyecte prompts durante una prueba normal. Sirve únicamente para estudiar el tipo de hook `prompt` en `sessionStart`. Para probarlo en Copilot CLI, habilita ese archivo conscientemente.

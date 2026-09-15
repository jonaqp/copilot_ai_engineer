# Guia de uso - Laboratorio de Hooks

## 1. Validar el baseline

```bash
python scripts/validate_workspace.py
```

Debe terminar con:

```text
RESULTADO: PASS
```

## 2. Ver todos los hooks sin Copilot

```bash
python scripts/simulate_hooks.py --all
```

El simulador envia payloads de ejemplo al mismo `hook_handler.py` utilizado por los hooks del repositorio.

## 3. Probar la politica principal

```bash
python scripts/run_demo_scenarios.py
```

Resultado esperado:

```text
HERRAMIENTA SEGURA     : allow
HERRAMIENTA PELIGROSA  : deny
ARGUMENTO CON SECRETO  : deny
CIERRE DEL AGENTE      : allow
RESULTADO               : PASS
```

## 4. Probar el agente

Seleccionar `hooks-governance-lab` y usar uno de los prompts de `PROMPT_EXAMPLES.md`.

## 5. Que observar

- El agente explica el objetivo antes de actuar.
- `preToolUse` toma decisiones deterministas.
- `postToolUse` agrega recomendaciones despues de cambios.
- `agentStop` ejecuta tests y puede bloquear la finalizacion.
- Los eventos quedan trazados en `.github/hooks/logs/audit.jsonl`.

## 6. Demo de fallo del quality gate

Cambiar temporalmente una expectativa en `demo_app/test_calculator.py` y ejecutar:

```bash
python scripts/simulate_hooks.py --event agentStop
```

Debe devolver `decision: block`. Restaurar el test y repetir; debe devolver `allow`.

## 7. Sobre `session-prompt-demo.json`

Viene con `disableAllHooks: true` para no inyectar prompts automaticamente durante una prueba normal. Sirve para estudiar el tipo de hook `prompt` en `sessionStart`. Habilitarlo solo de forma consciente cuando se quiera experimentar con ese comportamiento.

## 8. Idea clave

El agente razona; el hook gobierna una parte concreta del ciclo de vida con reglas deterministas.

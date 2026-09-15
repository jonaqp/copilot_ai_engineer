# GitHub Copilot Hooks Governance Lab - Carrito de compras

Laboratorio en español para aprender hooks de GitHub Copilot sin MCP. La aplicacion de demostracion es un carrito de compras local con productos, cantidades, stock, descuentos y checkout.

## Idea central

Los hooks no implementan la logica del carrito. Gobiernan **como trabaja el agente** sobre ese codigo:

```text
Prompt
  -> Agent
     -> preToolUse      (puede permitir/bloquear)
     -> Tool/Edit/Test
     -> postToolUse     (puede agregar contexto)
     -> agentStop       (ejecuta quality gate)
        -> PASS: termina
        -> FAIL: continua y corrige
```

## Inicio rapido

```bash
python demo_cart/demo.py
python -m unittest discover -s demo_cart -p "test_*.py"
python scripts/run_demo_scenarios.py
python scripts/simulate_hooks.py --all
python scripts/validate_workspace.py
```

Para comprender la organizacion de hooks, empezar por `.github/hooks/README.md`.

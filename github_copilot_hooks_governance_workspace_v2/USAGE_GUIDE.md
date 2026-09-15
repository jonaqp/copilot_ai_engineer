# Guia de uso

## 1. Entender el carrito

Abrir `demo_cart/cart.py`. Incluye `Product`, `CartItem`, `ShoppingCart` y `CheckoutService`.

Ejecutar:

```bash
python demo_cart/demo.py
python -m unittest discover -s demo_cart -p "test_*.py"
```

## 2. Entender los hooks por carpeta

Abrir `.github/hooks/README.md`.

- `01-session-audit.json`: observabilidad de sesion.
- `02-tool-guardrails.json`: seguridad y permisos sobre tools.
- `03-agent-lifecycle.json`: subagentes, errores y quality gate final.
- `scripts/hook_handler.py`: implementacion.
- `logs/audit.jsonl`: evidencia.

## 3. Ver escenarios controlados

```bash
python scripts/run_demo_scenarios.py
```

Muestra:
- comando de tests permitido;
- contexto agregado despues de una edicion;
- comando destructivo bloqueado;
- secreto bloqueado;
- `agentStop` permitido solo si los tests del carrito pasan.

## 4. Demo educativa de agentStop

Romper temporalmente una expectativa de `demo_cart/test_cart.py` y ejecutar:

```bash
python .github/hooks/scripts/hook_handler.py agentStop
```

El hook debe devolver `block`. Restaurar el test y repetir: debe devolver `allow`.

## 5. Validar todo

```bash
python scripts/validate_workspace.py
```

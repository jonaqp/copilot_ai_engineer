# Validation Report

Validaciones ejecutadas sobre el workspace:

- Grafo demo: PASS (10 componentes, 10 dependencias).
- Tests del motor: PASS (4 tests).
- Skill `dependency-graph-builder`: válido.
- Skill `change-impact-analyzer`: válido.
- Skill `risk-predictor`: válido.
- Skill `shift-left-gate`: válido.
- Escenario `pricing-service` + `contract`: detecta `checkout-api` y `cart-service` como dependientes directos, `storefront-web` como indirecto y la relación no documentada de `cart-service` como señal de riesgo.

La UI Flask está incluida, pero Flask no estaba instalado en el entorno de empaquetado; se ejecuta localmente tras `pip install -r requirements.txt`.

# Guía de uso

## 1. Instalar la demo

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
```

## 2. Ejecutar la aplicación web

```bash
python demo_arch_radar/app.py
```

Abrir `http://127.0.0.1:5000`.

## 3. Ejecutar análisis por CLI

```bash
python scripts/analyze_impact.py \
  --graph demo_arch_radar/sample_system/architecture.json \
  --component pricing-service \
  --change-type contract
```

Prueba también:

```bash
python scripts/analyze_impact.py --graph demo_arch_radar/sample_system/architecture.json --component order-db --change-type schema
```

## 4. Ejecutar el gate preventivo

```bash
python scripts/quality_gate.py \
  --graph demo_arch_radar/sample_system/architecture.json \
  --component order-db \
  --change-type schema \
  --tested checkout-api notification-service analytics-consumer
```

El script devuelve código distinto de cero si el cambio queda en NO-GO.

## 5. Usar el agente en GitHub Copilot

Selecciona `impact-radar` y prueba un prompt como:

> Analiza el impacto de cambiar la respuesta de `pricing-service`. Construye el mapa de dependencias, identifica efecto dominó, puntúa el riesgo y dime qué tests debo ejecutar antes del deploy. No modifiques código todavía.

Para un cambio real:

> Revisa el diff actual. Identifica las class y def modificadas, mapea qué componentes dependen de ellas directa o indirectamente y entrega GO / GO WITH CONDITIONS / NO-GO con evidencias.

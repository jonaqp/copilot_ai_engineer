# Functional Test Engineer - Guía de uso

Este workspace contiene un agente GitHub Copilot orientado a elevar y mantener coverage >=80% en proyectos Python/Flask mediante tests funcionales y de lógica.

## 1. Estructura

- `.github/agents/functional-test-engineer.agent.md`: agente principal.
- `.github/skills/`: skills especializadas.
- `reference-standards/`: estándares reutilizables.
- `demo_shop/`: aplicación Flask de carrito de compras.
- `tests/`: ejemplo de suite pytest.
- `scripts/`: coverage, gap analysis y quality gate.

## 2. Instalación demo

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## 3. Ejecutar la web

```bash
python run.py
```

Abrir `http://127.0.0.1:5000`.

## 4. Ejecutar tests y coverage

```bash
python scripts/run_quality_gate.py
```

Para analizar huecos:

```bash
python scripts/coverage_gap_report.py coverage.xml
```

## 5. Prompts recomendados para Copilot

### Subir coverage
> Usa el agente functional-test-engineer. Analiza `demo_shop/domain.py`, mide el coverage actual y agrega tests funcionales para dejar el módulo sobre 90% sin modificar producción salvo que sea estrictamente necesario.

### Probar una clase
> Revisa la clase `Cart`. Identifica estados, errores y bordes. Crea tests con pytest para add, update, remove, clear, stock y cantidades inválidas. Ejecuta el quality gate.

### Probar rutas Flask
> Usa flask-functional-testing para cubrir todas las rutas POST del carrito. Incluye caso feliz, error y recurso inexistente. No levantes servidor real.

### Analizar huecos
> Ejecuta coverage, usa coverage-gap-analyzer y dame los 5 comportamientos no cubiertos de mayor riesgo antes de escribir tests.

## 6. Flujo recomendado

Diagnóstico -> baseline -> priorización -> tests focalizados -> suite completa -> coverage -> gap report -> quality gate -> evidencia.

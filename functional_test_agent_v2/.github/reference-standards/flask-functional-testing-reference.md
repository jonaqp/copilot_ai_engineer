# Referencia de Testing Funcional Flask

## Fixture base
```python
import pytest
from demo_shop.app import create_app

@pytest.fixture
def app():
    app = create_app({"TESTING": True})
    yield app

@pytest.fixture
def client(app):
    return app.test_client()
```

## Patrón GET
```python
def test_home_renders_catalog(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Productos" in response.data
```

## Patrón POST
```python
def test_add_product_updates_cart(client):
    response = client.post("/cart/add/1", data={"quantity": "2"}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Carrito" in response.data
```

## Criterios
- No iniciar servidor real.
- Afirmar status code y efecto observable.
- Usar fixtures limpias.
- Probar errores de validación y 404.

import pytest


@pytest.fixture
def app():
    from demo_shop.app import create_app
    app = create_app({"TESTING": True, "SECRET_KEY": "test-secret"})
    yield app


@pytest.fixture
def client(app):
    return app.test_client()

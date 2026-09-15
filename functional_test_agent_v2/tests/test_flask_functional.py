def test_home_renders_catalog_and_cart_count(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Productos destacados" in response.data
    assert b"Aud\xc3\xadfonos Nova" in response.data
    assert b"Coverage target" in response.data


def test_home_filters_products_by_category(client):
    response = client.get("/?category=Video")
    assert response.status_code == 200
    assert b"Webcam Iris" in response.data
    assert b"Mouse Pulse" not in response.data


def test_add_to_cart_redirects_and_updates_cart(client, app):
    response = client.post("/cart/add/1", data={"quantity": "2"}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Carrito de compras" in response.data
    assert b"Aud\xc3\xadfonos Nova" in response.data
    assert app.extensions["cart"].item_count == 2


def test_add_invalid_quantity_shows_error(client, app):
    response = client.post("/cart/add/1", data={"quantity": "0"}, follow_redirects=True)
    assert response.status_code == 200
    assert b"quantity must be positive" in response.data
    assert app.extensions["cart"].item_count == 0


def test_add_unknown_product_returns_404(client):
    response = client.post("/cart/add/999", data={"quantity": "1"})
    assert response.status_code == 404


def test_update_cart_changes_quantity_and_zero_removes(client, app):
    client.post("/cart/add/2", data={"quantity": "1"})
    response = client.post("/cart/update/2", data={"quantity": "3"}, follow_redirects=True)
    assert response.status_code == 200
    assert app.extensions["cart"].item_count == 3

    client.post("/cart/update/2", data={"quantity": "0"})
    assert app.extensions["cart"].item_count == 0


def test_update_missing_product_reports_error(client):
    response = client.post("/cart/update/42", data={"quantity": "1"}, follow_redirects=True)
    assert response.status_code == 200
    assert b"product not in cart" in response.data


def test_remove_from_cart_and_missing_product(client, app):
    client.post("/cart/add/3", data={"quantity": "1"})
    response = client.post("/cart/remove/3", follow_redirects=True)
    assert response.status_code == 200
    assert app.extensions["cart"].item_count == 0
    assert b"Producto eliminado" in response.data

    missing = client.post("/cart/remove/3", follow_redirects=True)
    assert b"product not in cart" in missing.data


def test_checkout_empty_cart_returns_validation_message(client):
    response = client.post("/checkout", data={"customer_name": "Ana"}, follow_redirects=True)
    assert response.status_code == 200
    assert b"cart is empty" in response.data


def test_checkout_blank_customer_is_rejected(client):
    client.post("/cart/add/1", data={"quantity": "1"})
    response = client.post("/checkout", data={"customer_name": ""}, follow_redirects=True)
    assert response.status_code == 200
    assert b"customer name is required" in response.data


def test_checkout_success_renders_summary_and_clears_cart(client, app):
    client.post("/cart/add/4", data={"quantity": "2"})
    response = client.post("/checkout", data={"customer_name": "Jonathan"})
    assert response.status_code == 200
    assert b"Gracias, Jonathan" in response.data
    assert b"CHECKOUT COMPLETADO" in response.data
    assert app.extensions["cart"].item_count == 0

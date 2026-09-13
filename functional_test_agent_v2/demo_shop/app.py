from __future__ import annotations
from decimal import Decimal
from flask import Flask, abort, flash, redirect, render_template, request, url_for

from .domain import Catalog, Cart, CheckoutService, DiscountPolicy, PricingService, Product


def sample_products() -> list[Product]:
    return [
        Product(1, "Audífonos Nova", Decimal("49.90"), 8, "Audio", "Sonido claro y diseño liviano."),
        Product(2, "Teclado Orbit", Decimal("79.90"), 6, "Accesorios", "Teclado compacto para productividad."),
        Product(3, "Mouse Pulse", Decimal("34.50"), 10, "Accesorios", "Precisión y ergonomía para uso diario."),
        Product(4, "Webcam Iris", Decimal("119.00"), 4, "Video", "Video Full HD para reuniones y streaming."),
    ]


def create_app(test_config: dict | None = None) -> Flask:
    app = Flask(__name__)
    app.config.from_mapping(SECRET_KEY="demo-secret", TESTING=False)
    if test_config:
        app.config.update(test_config)

    catalog = Catalog(sample_products())
    cart = Cart()
    pricing = PricingService(DiscountPolicy(Decimal("150.00"), Decimal("0.10")))
    checkout_service = CheckoutService(pricing)

    app.extensions["catalog"] = catalog
    app.extensions["cart"] = cart
    app.extensions["pricing"] = pricing
    app.extensions["checkout_service"] = checkout_service

    @app.get("/")
    def home():
        category = request.args.get("category", "")
        products = catalog.by_category(category)
        return render_template("index.html", products=products, cart=cart, active_category=category)

    @app.get("/cart")
    def cart_view():
        return render_template("cart.html", cart=cart, totals=pricing.totals(cart))

    @app.post("/cart/add/<int:product_id>")
    def add_to_cart(product_id: int):
        try:
            product = catalog.get(product_id)
        except KeyError:
            abort(404)
        try:
            quantity = int(request.form.get("quantity", "1"))
            cart.add(product, quantity)
        except (TypeError, ValueError) as exc:
            flash(str(exc), "error")
            return redirect(url_for("home"))
        flash(f"{product.name} agregado al carrito", "success")
        return redirect(url_for("cart_view"))

    @app.post("/cart/update/<int:product_id>")
    def update_cart(product_id: int):
        try:
            quantity = int(request.form.get("quantity", "1"))
            cart.update(product_id, quantity)
        except (TypeError, ValueError, KeyError) as exc:
            flash(str(exc), "error")
        return redirect(url_for("cart_view"))

    @app.post("/cart/remove/<int:product_id>")
    def remove_from_cart(product_id: int):
        try:
            cart.remove(product_id)
            flash("Producto eliminado", "success")
        except KeyError as exc:
            flash(str(exc), "error")
        return redirect(url_for("cart_view"))

    @app.post("/checkout")
    def checkout():
        customer_name = request.form.get("customer_name", "")
        try:
            summary = checkout_service.checkout(cart, customer_name)
        except ValueError as exc:
            flash(str(exc), "error")
            return redirect(url_for("cart_view"))
        return render_template("success.html", summary=summary)

    return app


if __name__ == "__main__":
    create_app().run(debug=True)

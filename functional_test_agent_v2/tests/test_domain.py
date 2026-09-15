from decimal import Decimal
import pytest

from demo_shop.domain import (
    Cart,
    CartItem,
    Catalog,
    CheckoutService,
    DiscountPolicy,
    PricingService,
    Product,
    money,
)


def product(product_id=1, price="25.00", stock=5, category="Tech"):
    return Product(product_id, f"Product {product_id}", Decimal(price), stock, category, "Demo product")


@pytest.mark.parametrize(
    "raw, expected",
    [("1", Decimal("1.00")), (1.235, Decimal("1.24")), (Decimal("9.999"), Decimal("10.00"))],
)
def test_money_rounds_to_two_decimals(raw, expected):
    assert money(raw) == expected


@pytest.mark.parametrize(
    "kwargs, message",
    [
        ({"id": 0}, "product id must be positive"),
        ({"name": "   "}, "product name is required"),
        ({"price": Decimal("-1")}, "product price cannot be negative"),
        ({"stock": -1}, "product stock cannot be negative"),
    ],
)
def test_product_rejects_invalid_state(kwargs, message):
    data = dict(id=1, name="Keyboard", price=Decimal("10"), stock=2, category="Tech", description="x")
    data.update(kwargs)
    with pytest.raises(ValueError, match=message):
        Product(**data)


def test_product_in_stock_reflects_stock():
    assert product(stock=1).in_stock is True
    assert product(stock=0).in_stock is False


def test_cart_item_validates_quantity_and_calculates_subtotal():
    item = CartItem(product(price="12.50"), 2)
    assert item.subtotal == Decimal("25.00")
    with pytest.raises(ValueError, match="quantity must be positive"):
        CartItem(product(), 0)
    with pytest.raises(ValueError, match="quantity exceeds stock"):
        CartItem(product(stock=1), 2)


def test_cart_add_update_remove_and_totals():
    cart = Cart()
    p1 = product(1, "10.00", stock=5)
    p2 = product(2, "7.50", stock=5)
    cart.add(p1, 2)
    cart.add(p1, 1)
    cart.add(p2, 2)
    assert cart.item_count == 5
    assert cart.subtotal == Decimal("45.00")
    cart.update(1, 1)
    assert cart.item_count == 3
    cart.remove(2)
    assert cart.item_count == 1
    cart.clear()
    assert cart.items == []


def test_cart_update_zero_removes_and_missing_ids_raise():
    cart = Cart()
    cart.add(product(), 1)
    cart.update(1, 0)
    assert cart.item_count == 0
    with pytest.raises(KeyError, match="product not in cart"):
        cart.update(99, 1)
    with pytest.raises(KeyError, match="product not in cart"):
        cart.remove(99)


def test_cart_rejects_invalid_add_and_stock_overflow():
    cart = Cart()
    with pytest.raises(ValueError, match="quantity must be positive"):
        cart.add(product(), 0)
    with pytest.raises(ValueError, match="quantity exceeds stock"):
        cart.add(product(stock=1), 2)


def test_discount_policy_validates_configuration_and_threshold():
    with pytest.raises(ValueError, match="threshold cannot be negative"):
        DiscountPolicy(Decimal("-1"), Decimal("0.1"))
    with pytest.raises(ValueError, match="percent must be between 0 and 1"):
        DiscountPolicy(Decimal("10"), Decimal("1.1"))

    policy = DiscountPolicy(Decimal("100"), Decimal("0.10"))
    assert policy.discount_for(Decimal("99.99")) == Decimal("0.00")
    assert policy.discount_for(Decimal("100")) == Decimal("10.00")


def test_pricing_service_applies_discount_and_tax():
    cart = Cart()
    cart.add(product(price="200.00", stock=3), 1)
    pricing = PricingService(DiscountPolicy(Decimal("100"), Decimal("0.10")))
    totals = pricing.totals(cart)
    assert totals == {
        "subtotal": Decimal("200.00"),
        "discount": Decimal("20.00"),
        "tax": Decimal("34.20"),
        "total": Decimal("214.20"),
    }


def test_catalog_get_filter_and_missing_product():
    catalog = Catalog([product(1, category="Audio"), product(2, category="Video")])
    assert len(catalog.all()) == 2
    assert catalog.get(1).category == "Audio"
    assert [p.id for p in catalog.by_category("video")] == [2]
    assert len(catalog.by_category("")) == 2
    with pytest.raises(KeyError, match="product not found"):
        catalog.get(99)


def test_checkout_requires_customer_and_items_then_clears_cart():
    cart = Cart()
    service = CheckoutService(PricingService())
    with pytest.raises(ValueError, match="customer name is required"):
        service.checkout(cart, " ")
    with pytest.raises(ValueError, match="cart is empty"):
        service.checkout(cart, "Ana")

    cart.add(product(price="25"), 2)
    summary = service.checkout(cart, " Ana ")
    assert summary["customer"] == "Ana"
    assert summary["items"] == 2
    assert summary["total"] > Decimal("0")
    assert cart.item_count == 0

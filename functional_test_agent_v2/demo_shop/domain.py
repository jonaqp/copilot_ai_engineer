from __future__ import annotations
from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP


def money(value: Decimal | int | float | str) -> Decimal:
    return Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


@dataclass(frozen=True)
class Product:
    id: int
    name: str
    price: Decimal
    stock: int
    category: str
    description: str

    def __post_init__(self):
        if self.id <= 0:
            raise ValueError("product id must be positive")
        if not self.name.strip():
            raise ValueError("product name is required")
        if money(self.price) < 0:
            raise ValueError("product price cannot be negative")
        if self.stock < 0:
            raise ValueError("product stock cannot be negative")
        object.__setattr__(self, "price", money(self.price))

    @property
    def in_stock(self) -> bool:
        return self.stock > 0


@dataclass
class CartItem:
    product: Product
    quantity: int

    def __post_init__(self):
        if self.quantity <= 0:
            raise ValueError("quantity must be positive")
        if self.quantity > self.product.stock:
            raise ValueError("quantity exceeds stock")

    @property
    def subtotal(self) -> Decimal:
        return money(self.product.price * self.quantity)


class Cart:
    def __init__(self):
        self._items: dict[int, CartItem] = {}

    @property
    def items(self) -> list[CartItem]:
        return list(self._items.values())

    def add(self, product: Product, quantity: int = 1) -> None:
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        new_quantity = quantity
        if product.id in self._items:
            new_quantity += self._items[product.id].quantity
        self._items[product.id] = CartItem(product, new_quantity)

    def update(self, product_id: int, quantity: int) -> None:
        if product_id not in self._items:
            raise KeyError("product not in cart")
        if quantity == 0:
            self.remove(product_id)
            return
        self._items[product_id] = CartItem(self._items[product_id].product, quantity)

    def remove(self, product_id: int) -> None:
        if product_id not in self._items:
            raise KeyError("product not in cart")
        del self._items[product_id]

    def clear(self) -> None:
        self._items.clear()

    @property
    def item_count(self) -> int:
        return sum(item.quantity for item in self._items.values())

    @property
    def subtotal(self) -> Decimal:
        return money(sum((item.subtotal for item in self._items.values()), Decimal("0")))


class DiscountPolicy:
    def __init__(self, threshold: Decimal = Decimal("100.00"), percent: Decimal = Decimal("0.10")):
        self.threshold = money(threshold)
        self.percent = Decimal(str(percent))
        if self.threshold < 0:
            raise ValueError("threshold cannot be negative")
        if not Decimal("0") <= self.percent <= Decimal("1"):
            raise ValueError("percent must be between 0 and 1")

    def discount_for(self, subtotal: Decimal) -> Decimal:
        subtotal = money(subtotal)
        if subtotal >= self.threshold:
            return money(subtotal * self.percent)
        return money(0)


class PricingService:
    TAX_RATE = Decimal("0.19")

    def __init__(self, discount_policy: DiscountPolicy | None = None):
        self.discount_policy = discount_policy or DiscountPolicy()

    def totals(self, cart: Cart) -> dict[str, Decimal]:
        subtotal = cart.subtotal
        discount = self.discount_policy.discount_for(subtotal)
        taxable = subtotal - discount
        tax = money(taxable * self.TAX_RATE)
        total = money(taxable + tax)
        return {"subtotal": subtotal, "discount": discount, "tax": tax, "total": total}


class Catalog:
    def __init__(self, products: list[Product]):
        self._products = {p.id: p for p in products}

    def all(self) -> list[Product]:
        return list(self._products.values())

    def get(self, product_id: int) -> Product:
        try:
            return self._products[product_id]
        except KeyError as exc:
            raise KeyError("product not found") from exc

    def by_category(self, category: str) -> list[Product]:
        wanted = category.strip().lower()
        if not wanted:
            return self.all()
        return [p for p in self._products.values() if p.category.lower() == wanted]


class CheckoutService:
    def __init__(self, pricing: PricingService):
        self.pricing = pricing

    def checkout(self, cart: Cart, customer_name: str) -> dict[str, object]:
        if not customer_name.strip():
            raise ValueError("customer name is required")
        if not cart.items:
            raise ValueError("cart is empty")
        totals = self.pricing.totals(cart)
        summary = {
            "customer": customer_name.strip(),
            "items": cart.item_count,
            "total": totals["total"],
        }
        cart.clear()
        return summary

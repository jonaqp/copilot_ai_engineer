from dataclasses import dataclass, field
from pricing_service import PriceRequest, PricingService


@dataclass
class CartLine:
    sku: str
    quantity: int


@dataclass
class Cart:
    customer_tier: str = "standard"
    lines: list[CartLine] = field(default_factory=list)

    def add(self, sku: str, quantity: int = 1) -> None:
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        self.lines.append(CartLine(sku, quantity))


class CartService:
    def __init__(self, pricing: PricingService):
        self.pricing = pricing

    def total(self, cart: Cart):
        return sum(
            (self.pricing.quote(PriceRequest(line.sku, line.quantity, cart.customer_tier))["total"] for line in cart.lines),
            start=0,
        )

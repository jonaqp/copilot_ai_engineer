from dataclasses import dataclass
from decimal import Decimal


@dataclass
class PriceRequest:
    sku: str
    quantity: int
    customer_tier: str = "standard"


class DiscountPolicy:
    def percentage(self, customer_tier: str) -> Decimal:
        return Decimal("0.10") if customer_tier == "gold" else Decimal("0.00")


class PricingService:
    def __init__(self, policy: DiscountPolicy | None = None):
        self.policy = policy or DiscountPolicy()

    def unit_price(self, sku: str) -> Decimal:
        catalog = {"keyboard": Decimal("49.90"), "mouse": Decimal("19.90"), "monitor": Decimal("229.00")}
        if sku not in catalog:
            raise KeyError(sku)
        return catalog[sku]

    def quote(self, request: PriceRequest) -> dict:
        subtotal = self.unit_price(request.sku) * request.quantity
        discount = subtotal * self.policy.percentage(request.customer_tier)
        return {"subtotal": subtotal, "discount": discount, "total": subtotal - discount}

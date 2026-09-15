class LegacyInventoryMapper:
    def to_legacy_sku(self, sku: str) -> str:
        return f"LEG-{sku.upper()}"


class LegacyErpAdapter:
    def __init__(self, mapper: LegacyInventoryMapper | None = None):
        self.mapper = mapper or LegacyInventoryMapper()

    def synchronize_stock(self, sku: str, quantity: int) -> dict:
        return {"legacy_sku": self.mapper.to_legacy_sku(sku), "quantity": quantity, "status": "queued"}

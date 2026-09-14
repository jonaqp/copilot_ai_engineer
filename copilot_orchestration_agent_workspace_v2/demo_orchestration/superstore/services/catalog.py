from dataclasses import dataclass

@dataclass(frozen=True)
class Product:
    sku: str
    name: str
    price: float

CATALOG = {"KB-01": Product("KB-01", "Mechanical Keyboard", 89.90), "MS-02": Product("MS-02", "Wireless Mouse", 39.50)}

def get_product(sku: str) -> Product:
    if sku not in CATALOG:
        raise KeyError(f"Unknown SKU: {sku}")
    return CATALOG[sku]

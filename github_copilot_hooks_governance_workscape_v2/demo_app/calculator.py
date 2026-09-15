class Calculator:
    """Tiny domain class used to demonstrate hook-controlled code changes."""

    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("division by zero")
        return a / b

    def percentage(self, value: float, pct: float) -> float:
        return value * pct / 100

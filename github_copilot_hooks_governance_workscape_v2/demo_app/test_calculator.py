import unittest
from calculator import Calculator


class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(7, 2), 5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_divide(self):
        self.assertEqual(self.calc.divide(8, 2), 4)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(1, 0)

    def test_percentage(self):
        self.assertEqual(self.calc.percentage(200, 15), 30)


if __name__ == "__main__":
    unittest.main()

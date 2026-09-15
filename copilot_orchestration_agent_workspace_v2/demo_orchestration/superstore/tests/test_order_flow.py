import unittest
from demo_orchestration.superstore.services.orders import checkout

class OrderFlowTests(unittest.TestCase):
    def test_happy_path(self):
        r=checkout("KB-01",2,"tok_demo")
        self.assertEqual("CONFIRMED",r["status"])
        self.assertEqual(179.80,r["total"])
    def test_insufficient_stock(self):
        r=checkout("KB-01",99,"tok_demo")
        self.assertEqual("REJECTED",r["status"])
        self.assertEqual("insufficient_stock",r["reason"])
    def test_invalid_payment_token(self):
        r=checkout("MS-02",1,"bad")
        self.assertEqual("REJECTED",r["status"])
        self.assertEqual("invalid_token",r["reason"])

if __name__=="__main__": unittest.main()

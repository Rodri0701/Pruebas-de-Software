from src.main import ShoppingCart
from typing import List
import pytest, unittest

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_item(self):
        self.cart.add_item("appleR")
        self.assertEqual(self.cart.size(), 1)

    def test_remove_item(self):
    # Agregar algunos items a la lista
        self.cart.add_item("apple")
        self.cart.add_item("banana")
        self.cart.add_item("orange")
        self.assertEqual(self.cart.size(), 3)

        self.cart.remove_item("banana")
        self.assertEqual(self.cart.size(), 2)

        self.assertNotIn("banana", self.cart.get_items())

        
        self.cart.remove_item("grape")
        self.assertEqual(self.cart.size(), 2)


    def test_size(self):
        self.assertEqual(self.cart.size(), 0)
        self.cart.add_item("banana")
        self.assertEqual(self.cart.size(), 1)
        self.cart.add_item("orange")
        self.assertEqual(self.cart.size(), 2)

    def test_get_items(self):
        items = ["apple", "banana", "orange"]
        for item in items:
            self.cart.add_item(item)
        self.assertEqual(self.cart.get_items(), items)

if __name__ == '__main__':
    unittest.main()
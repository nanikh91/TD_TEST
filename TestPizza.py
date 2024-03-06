import unittest
from Pizza import Pizza

class TestPizza(unittest.TestCase):
    def test_pizza_creation(self):
        pizza = Pizza("Margarita", ["Tomato", "Mozzarella", "Basil"], 10.99)
        self.assertEqual(pizza.name, "Margarita")
        self.assertEqual(pizza.ingredients, ["Tomato", "Mozzarella", "Basil"])
        self.assertEqual(pizza.price, 10.99)

if __name__ == "__main__":
    unittest.main()
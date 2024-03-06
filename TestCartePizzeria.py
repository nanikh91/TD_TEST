import unittest
from unittest.mock import MagicMock
from CartePizzeria import CartePizzeria, Pizza, CartePizzeriaException

class TestCartePizzeria(unittest.TestCase):
    def setUp(self):
        # Créez une instance de la classe CartePizzeria pour chaque test
        self.carte = CartePizzeria()

    def test_is_empty_returns_true_when_no_pizzas(self):
        self.assertTrue(self.carte.is_empty())

    def test_is_empty_returns_false_when_pizzas_present(self):
        pizza_mock = MagicMock(spec=Pizza)
        self.carte.add_pizza(pizza_mock)
        self.assertFalse(self.carte.is_empty())

    def test_nb_pizzas_returns_correct_count(self):
        pizza_mock1 = MagicMock(spec=Pizza)
        pizza_mock2 = MagicMock(spec=Pizza)

        self.carte.add_pizza(pizza_mock1)
        self.carte.add_pizza(pizza_mock2)

        self.assertEqual(self.carte.nb_pizzas(), 2)

    def test_add_pizza_adds_pizza_to_list(self):
        pizza_mock = MagicMock(spec=Pizza)
        self.carte.add_pizza(pizza_mock)
        self.assertIn(pizza_mock, self.carte.pizzas)

    def test_remove_pizza_removes_pizza_by_name(self):
        pizza_mock1 = Pizza("Margarita", ["Tomato", "Mozzarella", "Basil"], 10.99)
        pizza_mock2 = Pizza("Pepperoni", ["Tomato", "Pepperoni", "Cheese"], 12.99)

        self.carte.add_pizza(pizza_mock1)
        self.carte.add_pizza(pizza_mock2)

        self.carte.remove_pizza("Margarita")

        self.assertEqual(self.carte.nb_pizzas(), 1)
        self.assertNotIn(pizza_mock1, self.carte.pizzas)

    def test_remove_pizza_raises_exception_if_not_found(self):
        with self.assertRaises(CartePizzeriaException) as context:
            self.carte.remove_pizza("Hawaiian")
        self.assertEqual(str(context.exception), "Pizza with name 'Hawaiian' not found")

if __name__ == "__main__":
    unittest.main()
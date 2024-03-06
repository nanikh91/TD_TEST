import unittest
from CartePizzeriaException import CartePizzeriaException

class TestCartePizzeriaException(unittest.TestCase):
    def test_exception_message(self):
        exception = CartePizzeriaException("Test exception message")
        self.assertEqual(str(exception), "Test exception message")

if __name__ == "__main__":
    unittest.main()
import unittest
from my_awesome_lib import math_tools

class TestMathTools(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(math_tools.factorial(5), 120)
        self.assertEqual(math_tools.factorial(0), 1)
        with self.assertRaises(ValueError):
            math_tools.factorial(-1)

    def test_is_prime(self):
        self.assertTrue(math_tools.is_prime(7))
        self.assertFalse(math_tools.is_prime(4))
        self.assertFalse(math_tools.is_prime(1))
        self.assertFalse(math_tools.is_prime(-5))
        self.assertFalse(math_tools.is_prime(2.5))

    def test_fibonacci(self):
        self.assertEqual(math_tools.fibonacci(6), 8)
        self.assertEqual(math_tools.fibonacci(0), 0)
        with self.assertRaises(ValueError):
            math_tools.fibonacci(-1)


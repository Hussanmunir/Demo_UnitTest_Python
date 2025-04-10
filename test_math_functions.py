import unittest
from math_functions import MathFunctions

class TestMathFunctions(unittest.TestCase):
    """Unit tests for MathFunctions."""

    def setUp(self):
        """Set up the MathFunctions instance."""
        self.math = MathFunctions()

    def test_add(self):
        """Test addition."""
        self.assertEqual(self.math.add(2, 3), 5)

    def test_subtract(self):
        """Test subtraction."""
        self.assertEqual(self.math.subtract(5, 3), 2)

    def test_multiply(self):
        """Test multiplication."""
        self.assertEqual(self.math.multiply(4, 3), 12)

    def test_divide(self):
        """Test division."""
        self.assertEqual(self.math.divide(10, 2), 5)

    def test_divide_by_zero(self):
        """Test division by zero."""
        with self.assertRaises(ValueError):
            self.math.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
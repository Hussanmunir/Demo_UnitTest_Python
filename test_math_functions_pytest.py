import pytest
from math_functions import MathFunctions

class TestMathFunctionsAdditionalPytest:
    """Additional Pytest test cases for MathFunctions."""

    def setup_method(self):
        """Setup for each test method."""
        self.math = MathFunctions()

    def test_add_large_numbers(self):
        """Test addition of large numbers."""
        assert self.math.add(1000000, 2000000) == 3000000

    def test_subtract_negative_numbers(self):
        """Test subtraction of negative numbers."""
        assert self.math.subtract(-5, -3) == -2

    def test_multiply_negative_numbers(self):
        """Test multiplication of negative numbers."""
        assert self.math.multiply(-4, -3) == 12

    def test_multiply_negative_numbers(self):
        """Test multiplication of negative numbers."""
        assert self.math.multiply(-4, -3) == 12

    def test_divide_negative_numbers(self):
        """Test division of negative numbers."""
        assert self.math.divide(-10, -2) == 5
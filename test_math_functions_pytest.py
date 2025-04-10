import pytest
from math_functions import MathFunctions

class TestMathFunctionsAdditionalPytest:
    """Additional Pytest test cases for MathFunctions."""

    @pytest.fixture
    def math(self):
        """Provide a MathFunctions instance for tests."""
        return MathFunctions()

    def test_add_large_numbers(self, math):
        """Test addition of large numbers."""
        assert math.add(1000000, 2000000) == 3000000

    def test_subtract_negative_numbers(self, math):
        """Test subtraction of negative numbers."""
        assert math.subtract(-5, -3) == -2

    def test_multiply_negative_numbers(self, math):
        """Test multiplication of negative numbers."""
        assert math.multiply(-4, -3) == 12

    def test_divide_negative_numbers(self, math):
        """Test division of negative numbers."""
        assert math.divide(-10, -2) == 5
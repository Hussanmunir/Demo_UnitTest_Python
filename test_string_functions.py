import unittest
from string_functions import StringFunctions

class TestStringFunctions(unittest.TestCase):
    """Unit tests for StringFunctions."""

    def setUp(self):
        """Set up the StringFunctions instance."""
        self.string = StringFunctions()

    def test_to_uppercase(self):
        """Test conversion of string to uppercase."""
        self.assertEqual(self.string.to_uppercase("hello"), "HELLO")

    def test_reverse_string(self):
        """Test reversal of string."""
        self.assertEqual(self.string.reverse_string("hello"), "olleh")

    def test_is_palindrome_true(self):
        """Test if a string is a palindrome (true case)."""
        self.assertTrue(self.string.is_palindrome("madam"))

    def test_is_palindrome_with_spaces(self):
        """Test if a string with spaces is a palindrome."""
        self.assertTrue(self.string.is_palindrome("A man a plan a canal Panama"))

    def test_is_palindrome_false(self):
        """Test if a string is a palindrome (false case)."""
        self.assertFalse(self.string.is_palindrome("hello"))
import pytest
from string_functions import StringFunctions

class TestStringFunctionsAdditionalPytest:
    """Additional Pytest test cases for StringFunctions."""

    def setup_method(self):
        """Setup for each test method."""
        self.string = StringFunctions()

    
    def test_to_uppercase_mixed_case(self):
        """Test conversion of mixed-case string to uppercase."""
        assert self.string.to_uppercase("HeLLo") == "HELLO"

    def test_reverse_string_with_spaces(self):
        """Test reversal of string with spaces."""
        assert self.string.reverse_string("hello world") == "dlrow olleh"

    def test_is_palindrome_case_insensitive(self):
        """Test if a string is a palindrome (case insensitive)."""
        assert self.string.is_palindrome("MadAm") is True

    def test_is_palindrome_with_special_characters(self):
        """Test if a string with special characters is a palindrome."""
        assert self.string.is_palindrome("A man, a plan, a canal: Panama") is True
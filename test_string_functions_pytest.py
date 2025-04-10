import pytest
from string_functions import StringFunctions

class TestStringFunctionsAdditionalPytest:
    """Additional Pytest test cases for StringFunctions."""

    @pytest.fixture
    def string(self):
        """Provide a StringFunctions instance for tests."""
        return StringFunctions()
    
    def test_to_uppercase_mixed_case(self, string):
        """Test conversion of mixed-case string to uppercase."""
        assert string.to_uppercase("HeLLo") == "HELLO"

    def test_reverse_string_with_spaces(self, string):
        """Test reversal of string with spaces."""
        assert string.reverse_string("hello world") == "dlrow olleh"

    def test_is_palindrome_case_insensitive(self, string):
        """Test if a string is a palindrome (case insensitive)."""
        assert string.is_palindrome("MadAm") is True

    def test_is_palindrome_with_special_characters(self, string):
        """Test if a string with special characters is a palindrome."""
        assert string.is_palindrome("A man, a plan, a canal: Panama") is True
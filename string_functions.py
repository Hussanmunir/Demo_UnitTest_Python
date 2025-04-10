import re

class StringFunctions:
    """A class containing basic string operations."""

    def to_uppercase(self, s):
        """Convert a string to uppercase."""
        return s.upper()

    def reverse_string(self, s):
        """Reverse the given string."""
        return s[::-1]

    def is_palindrome(self, s):
        """Check if a string is a palindrome."""
        s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())  # Remove non-alphanumeric characters and convert to lowercase
        return s == s[::-1]
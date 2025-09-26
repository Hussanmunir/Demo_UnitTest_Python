import unittest
from test_math_functions import TestMathFunctions
from test_string_functions import TestStringFunctions

class TestSuiteRunner:
    """Class to run all test cases in a suite."""

    @staticmethod
    def run():
        """Run all test cases written in unittest."""
        suite = unittest.TestSuite()
        suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestMathFunctions))
        suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestStringFunctions))
        # Note: TestMathFunctionsAdditionalPytest is a pytest test case and won't be added here.
        # suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestMathFunctionsAdditionalPytest))
    
        # Run the test suite
        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(suite)

if __name__ == "__main__":
    TestSuiteRunner.run()

    """
    pytest has backward compatibility with unittest but not vice versa.

    💡 Key takeaway:
        Use pytest as your universal runner. It can run both unittest and pytest-style tests, 
        giving you one combined report. This is the modern, clean approach.
    """
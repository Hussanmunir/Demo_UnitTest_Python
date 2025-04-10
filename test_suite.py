import unittest
from test_math_functions import TestMathFunctions
from test_string_functions import TestStringFunctions

class TestSuiteRunner:
    """Class to run all test cases in a suite."""

    @staticmethod
    def run():
        """Run all test cases."""
        suite = unittest.TestSuite()
        suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestMathFunctions))
        suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestStringFunctions))
    
        # Run the test suite
        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(suite)

if __name__ == "__main__":
    TestSuiteRunner.run()
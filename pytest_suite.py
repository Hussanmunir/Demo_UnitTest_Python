# pytest_runner_suite.py
import pytest

class PytestRunnerSuite:
    """Minimal runner to execute all pytest and unittest tests."""

    def run(self, test_files=None):
        """Run tests in the given files or current folder."""
        files = test_files if test_files else ["."]
        pytest.main(["-v"] + files)


if __name__ == "__main__":
    runner = PytestRunnerSuite()
    # Example: pass specific test files
    # runner.run(["test_math_unittest.py", "test_math_pytest.py"])
    
    # Or run all tests in current folder
    runner.run()
"""
This will run all tests, both unittest and pytest style, in the current directory.
"""
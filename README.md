# Demo Unit Test Python

This repository demonstrates unit testing in Python using both `unittest` and `pytest` frameworks. It includes examples of testing mathematical and string operations.

## Frameworks Used

### Pytest

Pytest is a powerful testing framework for Python that allows you to write simple as well as scalable test cases. It supports fixtures, parameterized testing, and has a rich ecosystem of plugins. Pytest is widely used for its simplicity and flexibility. For more details, refer to the [Pytest Documentation](https://docs.pytest.org/en/stable/).

### Unittest

Unittest is Python's built-in testing framework. It provides a test discovery mechanism and a rich set of assertions. It is ideal for writing structured and organized test cases in a class-based format. For more details, refer to the [Unittest Documentation](https://docs.python.org/3/library/unittest.html).

## Structure

- `LICENSE`: Contains the license information for the project.
- `math_functions.py`: Defines the `MathFunctions` class with basic mathematical operations such as addition, subtraction, multiplication, and division.
- `string_functions.py`: Defines the `StringFunctions` class with basic string operations such as converting to uppercase, reversing strings, and checking for palindromes.
- `test_math_functions.py`: Contains `unittest` test cases for the `MathFunctions` class.
- `test_string_functions.py`: Contains `unittest` test cases for the `StringFunctions` class.
- `test_math_functions_pytest.py`: Contains `pytest` test cases for the `MathFunctions` class.
- `test_string_functions_pytest.py`: Contains `pytest` test cases for the `StringFunctions` class.
- `unit_test_suite.py`: A test suite runner using `unittest` to execute all test cases.
- `pytest_test_suite.py`: A test suite runner using `pytest` to execute all test cases.
- `README.md`: Provides an overview of the project, including its structure, frameworks used, and instructions for running tests.

**Note: Pytest can handle test cases written in Unittest and Pytest style but not vice versa.**

## How to Run Tests

### Using Pytest

Run all tests:

```bash
pytest
```

Run a specific test file:

```bash
pytest test_math_functions_pytest.py
pytest test_string_functions_pytest.py
```

Run all pytest files from the test suite:

```bash
pytest test_suite.py
```

### Using Unittest

Run all tests in the test suite:

```bash
python test_suite.py
```

Run a specific test file:

```bash
python -m unittest test_math_functions.py
python -m unittest test_string_functions.py
```

## Generating HTML Coverage Report

To generate an HTML report for branch and statement coverage, follow these steps:

1. **Install `pytest-cov`:**
   Run the following command to install the `pytest-cov` plugin:
   ```bash
   pip install pytest-cov
   ```

2. **Run Tests with Coverage:**
   Use the following command to run your tests and generate an HTML report:
   ```bash
   pytest --cov=. --cov-report=html --cov-branch
   ```

   - `--cov=.`: Specifies the directory to measure coverage for (current directory in this case).
   - `--cov-report=html`: Generates an HTML report.
   - `--cov-branch`: Includes branch coverage in the report.

3. **View the Report:**
   After running the command, an `htmlcov` directory will be created in your workspace. Open the `index.html` file in a web browser to view the coverage report.

## Requirements

- Python 3.8 or higher
- `pytest` (install using `pip install pytest`)

## References

- [1] [Pytest Documentation](https://docs.pytest.org/en/stable/): Official documentation for the Pytest framework.
- [2] [Unittest Documentation](https://docs.python.org/3/library/unittest.html): Official documentation for Python's built-in Unittest framework.

import pytest
from project import info_quote_split, get_valid_input, get_inputs

def test_info_quote_split():
    # This function doesn't return anything, so we'll test if it runs without errors
    try:
        info_quote_split()
        assert True
    except Exception as e:
        assert False, f"An error occurred: {e}"

def test_get_valid_input():
    # Mocking input to test the function
    try:
        # Mocking input to return a valid integer
        with unittest.mock.patch('builtins.input', return_value='5'):
            result = get_valid_input("Test prompt: ")
            assert result == 5
    except Exception as e:
        assert False, f"An error occurred: {e}"

def test_get_inputs():
    # Mocking input to test the function
    try:
        # Mocking input to return valid integers
        with unittest.mock.patch('builtins.input', side_effect=['1', '2']):
            start, end = get_inputs()
            assert start == 1
            assert end == 2
    except Exception as e:
        assert False, f"An error occurred: {e}"

# Since the main function is the entry point and doesn't return anything,
# it's more challenging to test directly. You might consider refactoring
# your code to make it more testable, such as separating the logic into
# smaller functions that can be tested individually.
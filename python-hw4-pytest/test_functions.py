import pytest

from allFunctions import *

@pytest.mark.arithmetic
def test_add_int():
    assert add_int(2, 3) == 5
    assert add_int(-2, 3) == 1
    assert add_int(0, 0) == 0

@pytest.mark.arithmetic
def test_multiply_int():
    assert multiply_int(2, 3) == 6
    assert multiply_int(-2, 3) == -6
    assert multiply_int(0, 10) == 0

@pytest.mark.arithmetic
def test_divide_int():
    assert divide_int(6, 3) == 2
    assert divide_int(-6, 3) == -2
    assert divide_int(0, 10) == 0

    with pytest.raises(ValueError):
        divide_int(6, 0)

@pytest.mark.strings
def test_check_palindrome():
    assert check_palindrome("racecar") == True
    assert check_palindrome("hello") == False
    assert check_palindrome("") == True

@pytest.mark.strings
def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("12345") == "54321"
    assert reverse_string("") == ""

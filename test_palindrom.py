import pytest
from palindrom import is_palindrom


def test_palindrome_true():
    assert is_palindrom("madam") == True


def test_palindrome_false_1():
    assert is_palindrom("annu") == False


def test_palindrome_false_2():
    assert is_palindrom("week") == False

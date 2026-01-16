import pytest
from palindrom import is_palindrome


def test_palindrome_true():
    assert is_palindrome("madam") == True


def test_palindrome_false_1():
    assert is_palindrome("annu") == False


def test_palindrome_false_2():
    assert is_palindrome("week") == False

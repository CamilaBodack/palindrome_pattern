from django.test import TestCase
from .views import is_palindrome


class TestPalindromePattern(TestCase):
    word = 'anilina'

    def test_ispalindrome(self):
        assert is_palindrome('anilina')

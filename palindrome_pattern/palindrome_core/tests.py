from django.test import TestCase
from rest_framework.test import APIClient
from .views import is_palindrome


class TestPalindromePattern(TestCase):
    word = 'anilina'

    def test_ispalindrome(self):
        assert is_palindrome('anilina')

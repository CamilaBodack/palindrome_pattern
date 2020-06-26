#!/usr/bin/env python3


def is_palindrome(word):
    '''
        Function to verify palindrome pattern in string
        :param word: string to be verified
    '''

    if word == word[::-1]:
        return True
    else:
        return False

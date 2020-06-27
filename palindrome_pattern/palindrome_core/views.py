from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError


@api_view(["POST"])
def is_palindrome(request):

    """
        Function to verify palindrome pattern in string
        :param word: string to be verified
    """

    word = request.data.get("word")

    if word is None:
        return ValidationError("Data is empty")
    else:

        if word == word[::-1]:
            return Response({"Palindrome:": True})
        else:
            return Response({"Palindrome:": False})

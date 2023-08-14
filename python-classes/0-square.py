#!/usr/bin/python3


"""
Write a class Square that defines a square by:

    Private instance attribute: size
    Instantiation with size (no type/value verification)
    You are not allowed to import any module
"""


class square:
    """
    The class houses the attributes, and the methods/functions.

    Attributes:
        size(int): Which takes the arguments in integer.
    """

    def __init__ (self, size):
        """
        The __init__ method is part of the blueprint which takes an argument.
        Args:
            size(int): Which takes the arguments in integer.

        """
        self.__size = size
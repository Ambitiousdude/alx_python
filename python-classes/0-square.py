#!/usr/bin/python3
"""
Write a class Square that defines a square by:

    Private instance attribute: size
    Instantiation with size (no type/value verification)
    You are not allowed to import any module
"""

class Square:
    """
    A class representing a square.
    
    Attributes:
        size (int): The size of the square.

    Methods:
        __init__(self, size):
            Initializes the Square object with the given size.
    """
    def __init__(self, size):
        """
        Function/ method that initializes the object size.

        Args:
            size (int): The size of the square.
        """
        self.__Mysize = size
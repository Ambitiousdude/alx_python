#!usr/bin/python3

"""
Write a class Square that defines a square by:

Private instance attribute: size
Instantiation with size (no type/value verification)
You are not allowed to import any module
"""

class Square:
    """
    Represents a square with a private instance attribute 'size'.

    Attributes:
        size (int): The size of the square's sides.

    """
    def __init__(self, size):
        """
        Private attributes/variables that keeps the size private
        """
        self.Mysize= size
    
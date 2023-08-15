#!/usr/bin/python3
"""
Write a class Square that defines a square by: (based on 0-square.py)

Private instance attribute: size
Instantiation with optional size: def __init__(self, size=0):
size must be an integer, otherwise raise a TypeError exception 
with the message size must be an integer
if size is less than 0, raise a ValueError exception 
with the message size must be >= 0
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
    def __init__(self, size=0):
        """
        Private attribute: size
        Function/ method that initializes the object size.

        Args:
            size (int): The size of the square taking a value 0.

        Raises:
            TypeError: If the size provided is not an integer.
            ValueError: If the size provided is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size

    def area(self):
        """
        Calculate the area of the square sides.

        Return:  The current square area
        """
        return self._Square__size **2
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
        """
        self._Square__size = size
    @property
    def size(self):
        """
        An elegant way to retrieve data
        """
        return self._Square__size
    
    @size.setter
    def size(self, value):
        """
         An elegant way to set values

        Args:
            value (int): The new size for the square.

        Raises:
            TypeError: If the size provided is not an integer.
            ValueError: If the size provided is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value

    def area(self):
        """
        Calculates the area of the square and returns the new area.
        """
        return self._Square__size ** 2
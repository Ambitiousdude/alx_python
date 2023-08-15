#!/usr/bin/python3

"""
Write a class Square that defines a square by: (based on 3-square.py)

Private instance attribute: size:
    property def size(self): to retrieve it
    property setter def size(self, value): to set it:
        Raise a TypeError exception with the message size must be an integer
        Raise a ValueError exception with the message size must be >= 0
Instantiation with optional size: def __init__(self, size=0):
Public instance method: def area(self): that returns the current square area
Public instance method: def my_print(self): prints the square character #:
    if size is equal to 0, print an empty line
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
    
    def my_print(self):
        """
        Prints the square using the character '#'
        when the size is equal to 0, print a new line
        """
        if self._Square__size == 0:
            print("")
        else:
            for j in range(self._Square__size):
                print("#" * self._Square__size)
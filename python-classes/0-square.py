#!/usr/bin/python3

"""
Write a class Square that defines a square by:

Private instance attribute: size
Instantiation with size (no type/value verification)
You are not allowed to import any module
"""

class square:
    """
    The class is the blueprint that houses the attributes. 
    Also it houses the methods/functions.

    Attributes:
        size(int): The size is the attributes/variable of the object to be created
    """
    def __init__ (self, size):
      """
      The __init__ method takes the argument

      Args:
        size (int): The size of the square's sides.
      """
      self.__Mysize = size
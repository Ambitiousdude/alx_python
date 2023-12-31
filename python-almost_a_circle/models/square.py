#!/usr/bin/python3
"""
    Class Square that inherits from Rectangle
    Class constructor: def_init_(self,width,height,x=0,y=0,id=None)
        Calls the super class id,x,y,width and height
        Width and height must be assigned to the value size
        Creates new attributes for this class
        Inherit validation from Rectangle
    Overloading __str__ method should return: 
    [Square] (<id>) <x>/<y> - <size>
"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Inherits from Rectangle
    Class constructor:
        def _init_(self, size, x=0, y=0, id=None):
    The overloading __str__ method should return:
        [Square] (<id>) <x>/<y> - <size>
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Call super class with id, x, y, width and height
        Width, height, x and y validation must inherit from rectangle
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        A getter for size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        A setter for size
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        An overriding method
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
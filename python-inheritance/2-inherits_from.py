#!/usr/bin/python3

"""
Write a function that returns True if the object is an instance of a class 
that inherited (directly or indirectly) 
from the specified class ; otherwise False.
"""

def inherits_from(obj, a_class):
    """
    Parameters:
    obj : any
        The object to be checked for its class inheritance.
    a_class : class
        The class to be tested for the object's inheritance.

    Returns:
        bool:
            True if the object is an instance of a class that inherited
            (directly or indirectly) from the specified class; otherwise, False.
    """

    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
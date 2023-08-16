#!/usr/bin/python3
"""
Check if the given object is exactly an instance of the specified class.

Parameters:
obj : any
    The object to be checked if it's a member of the class.
a_class : class
    The class to check the object's membership.

Returns:
    bool:
        True if the object is exactly an instance of the specified class; otherwise, False.

Example:
>>> class Animal:
...     pass
...
>>> class Dog(Animal):
...     pass
...
>>> obj = Animal()
>>> is_same_class(obj, Animal)
True
>>> is_same_class(obj, Dog)
False
"""

def is_same_class(obj, a_class):
    """
    The method/function checks if the given object 
    is exactly an instance of the specified class.

    Parameters:
    obj : any
         The object to be checked if it's a member of the class.
    a_class : class
        The class to check the object's membership.

    Returns:
        bool:
            True if the object is exactly an instance of the specified class; otherwise, False.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
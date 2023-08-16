#!/usr/bin/python3

"""
Write a function that returns True if the object is an instance of, 
or if the object is an instance of a class that inherited from, 
the specified class ; otherwise False.
"""

def is_kind_of_class(obj, a_class):
    """
    Parameters:
        obj : any
            The object to be checked if it's a member of the class.
        a_class : class
            The class to check the object's membership.

        Returns:
            bool:
                True if the object is an instance of, or if the object is an instance of a class
                that inherited from, the specified class; otherwise, False.
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
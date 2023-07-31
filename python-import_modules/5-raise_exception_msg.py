#!/usr/bin/python3

# Raise an exception with a message

def raise_exception_msg(message=""):
    try:
         raise NameError(message) 
    except NameError as ne:
        print(ne)
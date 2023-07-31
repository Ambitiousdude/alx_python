#!/usr/bin/python3

# function definition
def safe_print_division(a, b):
# using try to test the code for errors 
    try:
        result = (a / b)
    # if b=0 raise a zerodivisionerror that prints none as a result
    except ZeroDivisionError:
        result = None
    except TypeError:
        print("Error: Please provide valid integers for both numbers.")
    # finally print inside result and return result
    finally:
        print("Inside result: {}".format(result))
    return result

#!/usr/bin/python3

# function definition
def safe_print_division(a, b):
# using try to test the code for errors 
    try:
        result = (a / b)
# handles the errors
    except:
        print("An exception has occured")
# execute the code regardless of the result of the try, and except
    finally:
       print("{}" .format(result))
    return None


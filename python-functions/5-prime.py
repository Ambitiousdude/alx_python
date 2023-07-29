#!/usr/bin/python3
def is_prime (number):
    number = int(input("Enter number: "))
    if number > 1:
        for i in range (2, number):
            if (number % i) == 0:
                return False
            
    else:
        return True

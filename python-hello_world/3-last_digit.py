#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if last_digit > 5:
    print("The last digit of {1} is {0} and is greater than 5" .format(last_digit, number))
elif last_digit == 0:
    print("The last digit of {1} is {0} and is 0" .format(last_digit, number))
elif last_digit < 6 and not 0:
    print("The last digit of {1} is {0} and is less than 6 and not 0" .format(last_digit, number))
else:
    print("end the program")
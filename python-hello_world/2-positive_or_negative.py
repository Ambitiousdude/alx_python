#!/usr/bin/python3
import random
number = random.randint(-10, 10)
for number in range(-10, 10):
   if number < 0:
      print("{} is negative" .format(number))
   else:
      print("{} is positive" .format(number))
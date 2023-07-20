#!/usr/bin/python3
import random
number = random.randint(-10, 10)
for number in range(-10, 10):
   if number > 0:
      print("{} is postive" .format(number))
   elif number == 0:
      print("{} is Zero" .format(number))
   else:
      print("{} is negative" .format(number), end="\n")

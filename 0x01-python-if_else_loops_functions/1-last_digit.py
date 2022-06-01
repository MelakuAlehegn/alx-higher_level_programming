#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    n = number * -1
else:
    n = number
r = n % 10
if r > 5:
    print("Last digit of", number, "is", r, "and is greater than 5")
elif r == 0:
    print("Last digit of", number, "is", r, "and is 0")
elif r < 6 and r != 0:
    print("Last digit of", number, "is", r, "and is less than 6 and not 0")

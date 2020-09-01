#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = abs(number) % 10
if number[-1:] == 0:
    print ("last digit of {:d} is {:d} and is 0".format(number, number[-1:]))
elif number[-1:] < 6:
    print ("last digit of {:d} is {:d} is less than 6 and not 0".format(number, number[-1:]))
else:
    print ("last digit of {:d} is {:d} and is greater than 5".format(number, number[-1:]))

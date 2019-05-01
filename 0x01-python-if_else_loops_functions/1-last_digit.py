#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
mod_n = number % 10

if number < 0:
    mod_n = (-(number) % 10) * -1

if mod_n > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, mod_n))
elif mod_n == 0:
    print("Last digit of {} is {} and is 0".format(number, mod_n))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(
        number, mod_n))

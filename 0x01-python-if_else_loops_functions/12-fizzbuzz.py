#!/usr/bin/python3
def fizzbuzz():
    n = range(1,101)
    for i in n:
        if ((i % 3 == 0) and (i % 5 == 0)):
            print("FizzBuzz ", end="")
        elif (i % 3 == 0):
            print("Fizz ", end="")
        elif (i % 5 == 0):
            print("Buzz ", end="")            
        else:
            print("{} ".format(i), end="")

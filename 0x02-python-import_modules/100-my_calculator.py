#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    ops = ["+", "-", "*", "/"]
    fcs = [add, sub, mul, div]
    for i in range(0, 4):
        if argv[2] == ops[i]:
            a = int(argv[1])
            b = int(argv[3])
            print("{:d} {:s} {:d} = {:d}".format(a, argv[2], b, fcs[i](a, b)))
            exit(0)
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

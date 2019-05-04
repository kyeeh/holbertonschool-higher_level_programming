#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    sum = 0
    ac = len(argv) - 1
    for i in range(1, ac + 1):
        sum += int(argv[i])
    print(sum)

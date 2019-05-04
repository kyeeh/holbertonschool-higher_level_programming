#!/usr/bin/python3
import sys

 if __name__ == "__main__":
    sum = 0
    ac = len(sys.argv) - 1
    for i in range(1, ac + 1):
        sum += int(sys.argv[i])
    print(sum)
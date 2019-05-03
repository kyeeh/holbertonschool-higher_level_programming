#!/usr/bin/python3
letters = range(ord('z'), ord('a') - 1, -1)
for i in letters:
    if (i % 2 == 0):
        print("{:c}".format(i), end="")
    else:
        print("{:c}".format(i - 32), end="")

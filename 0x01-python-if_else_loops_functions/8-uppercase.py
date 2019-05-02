#!/usr/bin/python3
def uppercase(str):
    for i in range(str.length):
        ucode = ord(str[i])
        if ucode >= 97 and ucode <= 122:
            print("{:c}".format(ord(str[i]) - 32), end="")
        else:
            print(str[i], end="")


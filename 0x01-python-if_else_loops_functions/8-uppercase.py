#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        ucode = ord(str[i])
        if ucode >= 97 and ucode <= 122:
            ucode = ucode - 32
        print("{:c}".format(ucode), end="")
    print()

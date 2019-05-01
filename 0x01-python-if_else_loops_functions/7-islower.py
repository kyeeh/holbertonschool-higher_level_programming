#!/usr/bin/python3
def islower(c):
    ucode = ord(c)
    if ucode >= 97 and ucode <= 122:
        return True
    return False

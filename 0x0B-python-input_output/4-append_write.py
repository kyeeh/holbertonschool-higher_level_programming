#!/usr/bin/python3
def append_write(filename="", text=""):
    """
    Writes a string to a text file and returns the number of characters written
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)

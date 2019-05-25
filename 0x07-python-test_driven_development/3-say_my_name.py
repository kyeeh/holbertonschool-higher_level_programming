#!/usr/bin/python3
"""
A function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    A function that prints My name is <first name> <last name>
    """
    str_msg1 = "first_name must be a string"
    str_msg2 = "last_name must be a string"
    if (is_str(first_name, str_msg1) and is_str(last_name, str_msg2)):
        print("My name is {:s} {:s}".format(first_name, last_name))


def is_str(e, msg):
    if (type(e) == str):
        return True
    else:
        raise TypeError(msg)

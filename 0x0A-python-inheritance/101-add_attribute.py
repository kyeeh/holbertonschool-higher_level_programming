#!/usr/bin/python3
def add_attribute(cls, field, name):
    if hasattr(cls, "__dict__"):
        setattr(cls, field, name)
    else:
        raise TypeError("can't add new attribute")

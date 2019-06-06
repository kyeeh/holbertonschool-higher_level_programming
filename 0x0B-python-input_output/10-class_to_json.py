#!/usr/bin/python3
def class_to_json(obj):
    """
    returns the dictionary description with simple data structure
    """
    return vars(obj)

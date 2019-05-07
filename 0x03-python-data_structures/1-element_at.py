#!/usr/bin/python3
def element_at(my_list, idx):
    size = len(my_list)
    if (idx < 0 or idx > size - 1):
        return (None)
    for i, e in enumerate(my_list):
        if (i == idx):
            return (e)

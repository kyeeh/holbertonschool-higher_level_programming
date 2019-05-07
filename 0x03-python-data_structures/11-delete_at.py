#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    size = len(my_list)
    if (idx >= 0 or idx < size):
        for i, e in enumerate(my_list):
            if (i == idx):
                my_list.remove(i + 1)
    return (my_list)

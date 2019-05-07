#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    size = len(my_list)
    new_list = list(my_list)
    if (idx >= 0 or idx < size):
        for i, e in enumerate(new_list):
            if (i == idx):
                new_list[i] = element
    return (new_list)

#!/usr/bin/python3
class MyList(list):
    """
    MyList class that inherits from list
    """
    def print_sorted(self):
        new_list = self[:]
        new_list.sort()
        print(new_list)

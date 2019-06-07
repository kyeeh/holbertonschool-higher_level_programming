#!/usr/bin/python3
class MyList(list):
    """
    MyList class that inherits from list
    """
    def print_sorted(self):
        new_list = list(sorted(self))
        print(new_list)
        return (new_list)

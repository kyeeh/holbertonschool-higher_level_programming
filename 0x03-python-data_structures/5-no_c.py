#!/usr/bin/python3
def no_c(my_string):
    s = my_string
    s = s.translate({ord('c'): None})
    s = s.translate({ord('C'): None})
    return (s)

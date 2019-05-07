#!/usr/bin/python3
def no_c(my_string):
    s = (my_string + '.')[:-1]
    s = s.replace("c", "")
    s = s.replace("C", "")
    return (s)

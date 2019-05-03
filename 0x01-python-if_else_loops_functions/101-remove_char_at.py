#!/usr/bin/python3
def remove_char_at(str, n):
    size = len(str)
    if (n < 0):
        return(str)
    return(str[0:n] + str[n + 1:size])

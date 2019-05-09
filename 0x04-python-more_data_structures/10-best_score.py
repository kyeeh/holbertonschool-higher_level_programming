#!/usr/bin/python3
"""
https://thepythonguru.com/python-builtin-functions/max/
"""


def best_score(a_dictionary):
    if (a_dictionary):
        return(max(a_dictionary, key=a_dictionary.get))

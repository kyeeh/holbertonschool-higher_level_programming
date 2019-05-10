#!/usr/bin/python3
def roman_to_int(roman_string):
    number = 0
    if (roman_string.__class__ == str):
        rss = len(roman_string)
        rdt = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        vlt = [rdt.get(value) for value in roman_string]
        for i, value in enumerate(vlt):
            if (i < rss - 1):
                if (value < vlt[i + 1]):
                    number -= value
                else:
                    number += value
            else:
                number += value
    return (number)

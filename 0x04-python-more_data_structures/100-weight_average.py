#!/usr/bin/python3
def weight_average(my_list=[]):
    num, den = 0, 0
    if (my_list and len(my_list) > 0):
        for (score, weight) in my_list:
            num += score * weight
            den += weight
        num /= den
    return (num)

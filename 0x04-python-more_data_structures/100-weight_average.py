#!/usr/bin/python3
def weight_average(my_list=[]):
    num, den = 0, 0
    if (my_list):
        for (score, weight) in my_list:
            num += score * weight
            den += weight
    return (num / den)

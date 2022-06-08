#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    mul = 0
    div = 0
    for n in my_list:
        mul += n[0] * n[1]
        div += n[1]
    return float(mul / div)

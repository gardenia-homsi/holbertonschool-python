#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    mul = 0
    sum = 0
    average = 0
    for a,b in zip(my_list):
        mul += a * b
        sum += b

    average = mul / sum
    return average

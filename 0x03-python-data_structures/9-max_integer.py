#!/usr/bin/python3
def max_integer(my_list=[]):
    n = 0
    if leng(my_list) == 0:
        return None
    else:
        for i in range(0, len(my_list)):
            if my_list[i] > n:
                n = my_list[i]
    return (n)

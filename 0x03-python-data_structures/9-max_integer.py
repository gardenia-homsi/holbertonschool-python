#!/usr/bin/python3
def max_integer(my_list=[]):
    max = 0
    if leng(my_list) == 0:
        return None
    else:
        for i in range(0, len(my_list)):
            if max > my_list[i]:
                max = max
        else:
            max = my_list[i]
    return max

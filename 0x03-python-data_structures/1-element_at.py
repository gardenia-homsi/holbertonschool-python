#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list) - 1:
        return (None)
    else:
        for i in range(0, len(my_list)):
            if i == idx:
                print("Element at index {:d} is {}".format(idx, my_list[i]))

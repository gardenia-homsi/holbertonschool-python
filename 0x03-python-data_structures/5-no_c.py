#!/usr/bin/python3
def no_c(my_string):
    for i in my_string:
        if ord(i) != 67 and ord(i) != 99:
            pass
    return my_string

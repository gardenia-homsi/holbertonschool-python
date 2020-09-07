#!/usr/bin/python3
def no_c(my_string):
    n = ""

    for i in my_string:
        if ord(i) != 67 and ord(i) != 99:
            n = n + i

    return(n)

#!/usr/bin/python3
def uppercase(str):
    i = 0
while i < len(str):
    val = ord(str[i])-32
    print("{:c}".format(val), end="")
    i += 1

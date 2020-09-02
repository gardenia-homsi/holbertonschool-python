#!/usr/bin/python3
str = ""
for i in reversed(range(97, 123)):
    if (i % 2) == 0:
        str += chr(i)
    else:
        str += chr(i - 32)
print("{}".format(str), end="")

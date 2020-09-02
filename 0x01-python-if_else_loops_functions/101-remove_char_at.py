#!/usr/bin/python3
def remove_char_at(str, n):
    s = ""
    count = 0
    for c in str:
        if count == n:
            pass
        else:
            s += c
        count += 1
    return s

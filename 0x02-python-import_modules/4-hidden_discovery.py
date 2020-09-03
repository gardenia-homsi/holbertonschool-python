#!/usr/bin/python3
import hidden_4
import os
if __name__ == '__main__':
    for fname in listdir(hidden_4):
        if fname[0] != '__':
            print(fname)

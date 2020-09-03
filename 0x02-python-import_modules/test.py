#!/usr/bin/python3
import file.pyc
import os
for fname  in os.listdir(file):
    if fname[0] != 'h':
        print(fname)

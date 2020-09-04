#!/usr/bin/python3
import sys
if len(sys.argv) > 1:
    print("{:d} arguments:".format(len(sys.argv) - 1))
    for i in range(1, len(sys.argv)):
        print("{:d}: {}".format(i, sys.argv[i]))
else:
    print("0 arguments.")

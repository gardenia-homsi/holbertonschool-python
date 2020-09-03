#!/usr/bin/python3
import sys
if len(sys.argv) == 0:
        print("0 arguments.")
else:
        print("{:d} arguments:".format(len(sys.argv)))
        for i in range (1, len(sys.argv)):
              print("{:d} : {}".format(i, sys.argv[i]))

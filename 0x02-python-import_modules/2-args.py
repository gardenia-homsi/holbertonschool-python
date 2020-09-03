#!/usr/bin/python3
import sys
if __name__ == '__main__':
        if len(sys.argv) == 1:
                print("0 arguments.")
        else:
                print("{:d} arguments:".format(len(sys.argv)))
                for i in range(2, len(sys.argv)):
                        print("{:d} : {}".format(i, sys.argv[i]))

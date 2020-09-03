#!/usr/bin/python3
import sys
if __name__ == '__main__':
        if len(sys.argv) == 1:
                print("0 arguments.")
        else:
                for i in range(1, len(sys.argv)):
                        print("{:d} : {}".format(i, sys.argv[i]))

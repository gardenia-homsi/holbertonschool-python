#!/usr/bin/python3
import sys
        if len(sys.argv) == 1:
                if __name__ == '__main__':
                print("0 arguments.")
        else:
                if __name__ == '__main__':
                print("{:d} arguments:".format(len(sys.argv) - 1))
                for i in range(1, len(sys.argv)):
                        print("{:d} : {}".format(i, sys.argv[i]))

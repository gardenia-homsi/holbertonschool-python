#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("error")
        exit(1)
    else:
        if sys.argv[2] == "+":
            print("{:d} + {:d} = {:d}".format(sys.argv[1], sys.argv[3], add(sys.argv[1], sys.argv[3])))
            exit(0)
        elif sys.argv[2] == "-":
            print("{:d} - {:d} = {:d}".format(sys.argv[1], sys.argv[3], add(sys.argv[1], sys.argv[3])))
            exit(0)
        elif sys.argv[2] == "*":
            print("{:d} * {:d} = {:d}".format(sys.argv[1], sys.argv[3], add(sys.argv[1], sys.argv[3])))
            exit(0)
        elif sys.argv[2] == "/":
            print("{:d} / {:d} = {:d}".format(sys.argv[1], sys.argv[3], add(sys.argv[1], sys.argv[3])))
            exit(0)
        else:
            print("not operator")

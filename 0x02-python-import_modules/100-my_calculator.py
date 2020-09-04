#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
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
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)

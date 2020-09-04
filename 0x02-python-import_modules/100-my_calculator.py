#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import *
    a = 0
    val = False
    op = {"+": add, "-": sub, "*": mul, "/": div}

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        for i in op:
            if argv[2] == i:
                a = op[i](int(argv[1]), int(argv[3]))
                val = True
                break

    if val is False:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print(str(argv[1]), "{}".format(i), str(argv[3]), "= {:d}".format(a))
    exit(0)

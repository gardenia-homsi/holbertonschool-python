#!/usr/bin/python3
import sys
sum = 0
if __name__ == '__main__':
    for i in range(1, len(sys.argv)):
        sum += int(sys.argv[i])
print(sum)

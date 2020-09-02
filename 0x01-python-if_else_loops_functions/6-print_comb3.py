#!/usr/bin/python3
for i in range(0, 9):
    for j in range (1,8):
        if (i != j):
            print("{:d}{:d},".format(i, j), end=" ")
print ("{:d}{:d}".format(i+1,j+1))

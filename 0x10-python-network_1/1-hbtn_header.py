#!/usr/bin/python3
"""displays the value of the X-Request-Id variable found in the header of the r
esponse"""


from urllib import (request)
from sys import argv

if __name__ == '__main__':
    with request.urlopen(argv[1]) as header:
        print(header.getheader('X-Request-Id'))

#!/usr/bin/python3
"""manage urllib.error.HTTPError exceptions"""


from urllib import (request, parse, error)
from sys import argv

if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as response:
            body = response.read()

        print(body.decode('utf8'))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))

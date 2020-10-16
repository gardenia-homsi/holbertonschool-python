#!/usr/bin/python3
"""
    2-post_email.py
"""

from urllib import (request, parse)
from sys import argv

if __name__ == "__main__":
    values = {}
    values["email"] = argv[2]
    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        body = response.read()

    print(body.decode('utf8'))

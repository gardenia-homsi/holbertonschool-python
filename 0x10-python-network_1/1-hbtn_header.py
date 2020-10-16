#!/usr/bin/python3
"""
    1-hbtn_header.py
"""

from urllib import (request)
from sys import argv

if __name__ == "__main__":
    req = request.Request(argv[1])
    with request.urlopen(req) as response:
        header = response.info()

    print(header.get("X-Request-Id"))

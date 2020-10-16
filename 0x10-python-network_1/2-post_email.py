#!/usr/bin/python3
"""
    POST request to the passed URL with the email as a parameter
"""


from urllib import (request, parse)
from sys import argv

if __name__ == "__main__":
    values = {'email': argv[2]}
    data = parse.urlencode(values)
    data = data.encode('ascii')
    url = request.Request(argv[1], data)

    with request.urlopen(url) as response:
        response = response.read()
        print(response.decode('utf8'))

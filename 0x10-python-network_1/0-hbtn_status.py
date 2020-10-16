#!/usr/bin/python3
"""this model is to fetch internet resources"""


from urllib import (request)

if __name__ == "__main__":
    req = request.Request("https://intranet.hbtn.io/status")
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()

    print("Body Response:\n\t- type: {}\n\t - content: {}".format(type(html), 
    html))
    print("\t- utf8 content: {}".format(str(type, 'utf-8')))

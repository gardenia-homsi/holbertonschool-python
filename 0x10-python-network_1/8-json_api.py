#!/usr/bin/python3
"""
    8-json_api.py
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) == 2:
        r = requests.post(url, data={'q': argv[1]})
    else:
        r = requests.post(url, data={'q': ""})
    try:
        obj_js = r.json()
        if obj_js:
            print("[{}] {}".format(obj_js.get("id"), obj_js.get("name")))
        else:
            print("No result")
    except:
        print("Not a valid JSON")

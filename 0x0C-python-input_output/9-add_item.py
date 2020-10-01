#!/usr/bin/python3
"""
Python function that add arguments to a Python list
"""
import sys
import os.path

save_json = __import__('7-save_to_json_file').save_to_json_file
load_json = __import__('8-load_from_json_file').load_from_json_file

list_1 = []

if not os.path.exists("./add_item.json"):
    save_json(list_1, "add_item.json")

list_1 = load_json("add_item.json")

for i in sys.argv[1:]:
    list_1.append(i)

save_json(list_1, "add_item.json")

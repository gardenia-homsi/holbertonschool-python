#!/usr/bin/python3
""" Load, add, save """


import sys
import os

load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file


my_list = []
if not os.path.exists("./add_item.json"):
    save_to_json_file(list_1, "add_item.json")
my_list = load_from_json_file("add_item.json")
for i in range(1, len(argv)):
    my_list.append((argv[i]))
save_to_json_file(my_list, "add_item.json")

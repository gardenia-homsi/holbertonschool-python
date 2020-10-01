#!/usr/bin/python3
""" Load, add, save """


import json
import os
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file


my_list = []
if not os.path.exists("./add_item.json"):
    save_json(list_1, "add_item.json")
for i in range(0, argv):
    my_list.append(load_from_json_file(argv[i]))
save_to_json_file(my_list, "add_item.json")

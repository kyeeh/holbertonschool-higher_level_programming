#!/usr/bin/python3
from sys import argv
"""
Adds all arguments to a Python list, and then save them to a file
"""


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
    arg = load_from_json_file("add_item.json")
except:
    arg = []
for i in range(1, len(argv)):
    arg.append(argv[i])

save_to_json_file(arg, "add_item.json")

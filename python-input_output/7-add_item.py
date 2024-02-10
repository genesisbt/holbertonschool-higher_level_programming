#!/usr/bin/python3
"""
module to add all arguments to a python list and save to a file
"""

from sys import argv
import json
save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file

try:
    lista = load("add_item.json")
except FileNotFoundError:
    lista = []

    for argnum in range(1, len(argv)):
        lista.append(argv[argnum])
save(lista, "add_item.json")

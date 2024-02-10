#!/usr/bin/python3
"""
module to add all arguments to a python list and save to a file
"""
from sys import argv
save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file
filename = "add_item.json"

try:
    lista = load(filename)
except FileNotFoundError:
    lista = []

    for argnum in range(1, len(argv)):
        lista.append(argv[argnum])
save(lista, filename)

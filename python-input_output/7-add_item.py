#!/usr/bin/python3
"""
module to add all arguments to a python list and save to a file
"""
from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


try:
    lista = load_from_json_file("add_item.json")
except FileNotFoundError:
    lista = []

    for argnum in range(1, len(argv)):
        lista.append(argv[argnum])
save_to_json_file(lista, "add_item.json")

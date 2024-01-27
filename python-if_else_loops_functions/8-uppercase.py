#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            char = chr(ord(char) - ord('a') + ord('A'))
        result += char
    print("{}".format(result), end = '\n')

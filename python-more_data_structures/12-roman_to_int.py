#!/usr/bin/python3
def roman_to_int(roman_string):
    newint = 0
    if roman_string == None or type(roman_string) != str:
        return 0
    for index in range(len(roman_string)):
        newint = add(roman_string[index], newint)
        if index < len(roman_string) -1:
            if roman_string[index] == "I" and roman_string[index + 1] != "I":
                newint = newint - 2
    return newint

def add(char, n1):
    n2 = 0
    if char == "M":
        n2 = n1 + 1000
    if char == "D":
        n2 = n1 + 500
    if char == "C":
        n2 = n1 + 100
    if char == "L":
        n2 = n1 + 50
    if char == "X":
        n2 = n1 + 10
    if char == "V":
        n2 = n1 + 5
    if char == "I":
        n2 = n1 + 1
    return n2;

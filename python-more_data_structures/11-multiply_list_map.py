#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    newlist = my_list.copy()
    newlist = list(map(lambda x: multiply(x, number), newlist))
    return newlist
    
def multiply(number1, number2):
    newnumber = number1 * number2 
    return newnumber

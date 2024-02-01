#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for index in range(x):
        if index < len(my_list):
            print("{}".format(my_list[index], end=""))
    if x < len(my_list):
        return x
    return len(my_list)

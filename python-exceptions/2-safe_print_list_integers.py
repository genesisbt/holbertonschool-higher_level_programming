#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nprint = 0
    for index in range(x):
        try:
            print("{:d}".format(my_list[index]), end="")
            nprint += 1
        except (IndexError, TypeError, ValueError):
            continue
    print()
    return nprint

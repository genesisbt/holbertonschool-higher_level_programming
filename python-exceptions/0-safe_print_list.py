#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for index in range(x):
            print("{}".format(my_list[index]), end="")
    except IndexError:
       print()
       return index

    print()
    return index + 1

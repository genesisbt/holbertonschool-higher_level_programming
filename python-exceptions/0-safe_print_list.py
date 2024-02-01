#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if not my_list:
        return 0
    for index in range(x):
        try:
            print(my_list[index], end="")
        except IndexError:
            index = index - 1
            break
    print()
    return index + 1 

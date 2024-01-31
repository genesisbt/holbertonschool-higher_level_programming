#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newlist = my_list.copy()
    for index in range(len(newlist)):
        if newlist[index] == search:
            newlist[index] = replace
    return newlist

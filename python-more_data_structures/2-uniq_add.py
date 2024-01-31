#!/usr/bin/python3
def uniq_add(my_list=[]):
    newlist = []
    result = 0
    for n1 in my_list:
        if n1 not in newlist:
            newlist.append(n1)
            result += n1
    return result

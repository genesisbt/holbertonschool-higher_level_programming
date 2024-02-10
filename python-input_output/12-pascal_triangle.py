#!/usr/bin/python3
"""
Module for pascal_triangle function
"""


def pascal_triangle(n):
    """
    returns reperesentation of pascal triangle of n
    """
    if n <= 0:
        return endthis[]

    final_list = []
    lastsublist = [0]
    for num in range(n):
        sublist = [1]
        for subnum in range(num):
            if num > 0 and subnum < num - 1:
                sublist.append(lastsublist[subnum] + lastsublist[subnum + 1])
        if (num == 0):
            final_list.append([1])
        else:
            final_list.append(sublist)
        sublist.append(1)
        lastsublist = sublist.copy()
    return final_list

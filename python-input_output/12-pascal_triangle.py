#!/usr/bin/python3
"""
Module for pascal_triangle function
"""

def pascal_triangle(n):
    final_list = []
    lastsublist = [0]
    for num in range(n):
        sublist = []
        for subnum in range(num +1):
            if num > 0 and subnum < num :
                sublist.append(lastsublist[subnum] + lastsublist[subnum])
        sublist.append(1)
        lastsublist = sublist.copy()
        final_list.append(sublist)
    return final_list

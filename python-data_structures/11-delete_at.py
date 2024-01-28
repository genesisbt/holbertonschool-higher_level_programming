#!/usr/bin/python3
def delete_at(my_list=[], idx=0, modify=False):
    if idx >= 0 and idx < len(my_list):
        if modify:
            del my_list[idx]
        else:
            return my_list[:idx] + my_list[idx+1:]
        elif modify:
            return my_list
        else:
            return my_list[:]

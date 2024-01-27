#!/usr/bin/python3
for d1 in range(0, 10):
    for d2 in range(d1, 10):
        if d1 != d2:
            print("{}{}".format(d1, d2), end=', ' if d1 != 8 or d2 != 9 else '\n')

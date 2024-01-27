#!/usr/bin/python3
for d in range(0, 10):
    for e in range(d, 10):
        if d != e:
            print("{}{}".format(d, e), end=', ' if d != 8 or e != 9 else '\n')

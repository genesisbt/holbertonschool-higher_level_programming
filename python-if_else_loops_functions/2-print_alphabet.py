#!/usr/bin/python3
for code in range(ord('a'), ord('z') +1):
    if chr(code) != 'q' and chr(code) != 'e':
        print(f"{chr(code)}")

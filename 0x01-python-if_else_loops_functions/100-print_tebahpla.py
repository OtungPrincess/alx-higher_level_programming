#!/usr/bin/python3
for n in reversed(range(97, 123)):
    if(n % 2 == 0):
        print(chr(n), end='')
    else:
        print(chr(n - 32), end='')

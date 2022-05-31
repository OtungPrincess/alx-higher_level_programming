#!/usr/bin/python3
for i in range(26):
    if (i != 16 and i != 4):
        print("{:c}" .format(ord("a")+i), end='')

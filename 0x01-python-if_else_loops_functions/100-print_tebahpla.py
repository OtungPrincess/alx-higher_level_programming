#!/usr/bin/python3
for n in range(ord('z'), ord('a') - 1, -2):
    print("{:c}{:s}".format(n, chr(n - 33)), end='')

#!/usr/bin/python3
"""Reads from standard input and computes metrics.
After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


from sys import stdin


status_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
        }

size = i = 0


def printer():
    '''prints the statistics'''
    print("File size: {}".format(size))
    for key, value in sorted(status_codes.items()):
        if value > 0:
            print('{:s}: {:d}'.format(key, value))


try:
    for line in stdin:
        split_line = line.split()
        if len(split_line) >= 2:
            stats = split_line[-2]
            size += int(split_line[-1])
            if stats in status_codes:
                status_codes[stats] += 1
        i += 1

        if i % 10 == 0:
            printer()
    printer()
except KeyboardInterrupt as e:
    printer()

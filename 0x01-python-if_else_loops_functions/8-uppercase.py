#!/usr/bin/python3
def uppercase(str):
    for n in str:
        lt = ord(n)
        if lt >= 97 and lt <= 122:
            n = chr(lt - 32)
        print("{}".format(n), end='')
    print("")

#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argv_1 = len(argv) - 1
    if(argv_1 == 0):
        print("0 arguments.")
    elif(argv_1 == 1):
        print(f"{argv_1} argument:")
    elif(argv_1 > 1):
        print(f"{argv_1} arguments:")
    for n in range(1, argv_1 + 1):
        print(f"{n}: {argv[n]}")

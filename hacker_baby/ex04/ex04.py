#!/usr/bin/env python3
import sys


def init():
    if len(sys.argv) == 1:
        print("No input detected")
        exit()
    else:
        if sys.argv[1].isnumeric() is True:
            if int(sys.argv[1]) < 1:
                # print("\n")
                exit()
            else:
                val = int(sys.argv[1])
                return val
        else:
            # print("\n")
            exit()


def primefinder(val, arr):

    if val == 1:
        print("1")
    else:
        # print('a' + str(val))
        for num in range(2, val):
            if val % num == 0:
                # print(num)
                arr = arr + str(num) + ","
                return primefinder(round(val/num),arr)
        arr = arr + str(val)
        print(arr)



def main():
    init()
    arr = ''
    primefinder(init(), arr)


main()

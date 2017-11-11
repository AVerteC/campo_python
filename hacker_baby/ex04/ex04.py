#!/usr/bin/env python3
import sys


def init():
    if len(sys.argv) == 1:
        print("No input detected")
        exit()
    else:
        if sys.argv[1].isnumeric() is True:
            if int(sys.argv[1]) < 1:
                print("\n")
                exit()
        else:
            print("\n")
            exit()


def primefinder():
    val = int(sys.argv[1])
    if val == 1:
        print("1")
    else:
        for num in range(1, val):
            stage2 = val/num
            print(stage2/num)



def main():
    init()
    primefinder()


main()

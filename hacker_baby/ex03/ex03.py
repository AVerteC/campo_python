#!/usr/bin/env python3
import sys


def init():
    uptosum = sys.argv[1]
    if uptosum is not int or float:
        print("Program input is not valid")
    else:
        return uptosum


def multiplestosum(uptosum):
    [i for i in range(1000) if i % 3 == 0 or i % 5 == 0]

    print(uptosum)


def main():
    multiplestosum(init())


main()

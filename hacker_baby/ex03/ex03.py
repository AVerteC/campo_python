#!/usr/bin/env python3
import sys


def init():
    if len(sys.argv) == 1:
        print("No input detected")
        exit()
    else:
        if sys.argv[1].isnumeric() is True:
            pass
        else:
            print("Input is not an integer")
            exit()

def multiplestosum():
    uptosum = int(sys.argv[1])
    all = 0
    if uptosum < 0:
        uptosum = str(uptosum)
        uptosum = uptosum.replace('-', '')
        uptosum = int(uptosum)
        for num in range(uptosum):
            if num % 3 == 0 or num % 5 == 0:
                all += num
        print('-' + str(all))
    else:
        for num in range(uptosum):
            if num % 3 == 0 or num % 5 == 0:
                all += num
        print(all)


def main():
    init()
    multiplestosum()


main()

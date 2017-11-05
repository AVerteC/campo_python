#!/usr/bin/env python3
# made by Alan CHen
import re

a = 'abcdefghsijsklsmsnospqsrstuvwxyz'
# there are seven 's' characters


def sfinder(a):
    return re.findall('s', a)


def main():
    print(sfinder(a))


main()

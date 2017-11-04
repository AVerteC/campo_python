#!usr/bin/env python3

import sys
def init():
    listo = sys.argv[1:]
def arr():
        num = 0
        global listo
        listo = sys.argv[1:]
        for i in listo:
            num +=1
            print("Argv of {0} is {1}".format(num, i))


def lensort():
        # lambda x: len(x) replaces a def s(x): return len(x)
        slisto = sorted(listo, key=lambda x: len(x),reverse=True)
        for i in slisto:
            print(i)
















def main():
        arr()
        lensort()

main()
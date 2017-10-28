#!usr/bin/env python3
#made by alan chen
import sys


def init():
    global d1
    global inputs
    global list1
    # set up inputs
    inputs = sys.argv
    inputs.remove('4204_arr.py')
    inputs = list(map(float, inputs))
    list1 = inputs

def rangee():
    #calculate range
        rangee = max(list1)-min(list1)
        print("Range: ", round(rangee, 4))

def main():
    init()
    rangee()

main()
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


def mean():
    #calculate mean
        mean = sum(list1)/len(list1)
        print("Mean: ", round(mean, 4))

def main():
    init()
    mean()

main()
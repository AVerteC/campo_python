#!usr/bin/env python3
# made by Alan Chen
from collections import Counter
import sys


def init():

        global d1
        global inputs
        global list1

        # set up inputs
        inputs = sys.argv

        # remove the program name from the list from argv
        inputs.remove('4204_arr.py')

        # use map to make all of the elements in the inputs list a float
        inputs = list(map(float, inputs))

        list1 = inputs
        # use map to make all of the elements in the inputs list a float
        inputsmode = list(map(float, inputs))
        d1 = dict(Counter(inputsmode))


def mode():
    # calculate modes
        modes = list()
        for k, v in d1.items():
            if v >= 2:
                modes.append(k)


        mode = str(modes)
        marr = [str(a) for a in modes]
        print('Mode: ', end='')
        print(", " . join(marr))

# make a counter which pipes out to a list
# then print out the list
# but also exclude when there is no mode
def rangee():
    # calculate range
        rangee = max(list1)-min(list1)
        print("Range: ", round(rangee, 4))

def mean():
    # calculate mean
        mean = sum(list1)/len(list1)
        print("Mean: ", round(mean, 4))


def median():
    # calculate the median with indexes, but calculate the point in the center of the list if the list is even
    if (len(inputs) % 2 == 0):
        inputs.sort()
        mathas = len(inputs)/2
        mathan = int(len(inputs)/2)-1
        median = (mathas + mathan)/2
    else:
        mathas = len(inputs)/2
        median = mathas

    outs = round(median, 4)
    print("Median: ", outs)


def minimum():
        print("Min: ", min(list1))


def maximum():
        print("Max: ", max(list1))


def main():
    init()
    minimum()
    maximum()
    median()
    mode()
    rangee()






main()

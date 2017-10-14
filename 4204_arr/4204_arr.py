#!usr/bin/env python3
from collections import Counter
import sys
inputs = sys.argv

inputs.remove('4204_arr.py')
inputs = list(map(int, inputs))
d1= dict(Counter(inputs))
list1 = inputs
print(d1)
modes = list()
for k, v in d1.items():
    if v >= 2:
        modes.append(k)

print(modes)

'''
make a counter which pipes out to a list
then print out the list
but also exclude when there is no mode
'''

mean = sum(list1)/len(list1)
mathas = len(list1)/2

if (len(list1) % 2 == 0):
    list1.sort()
    mathan = int(len(list1)/2)-1

    median = (mathas + mathan)/2

else:
    median = mathas




rangee = max(list1)-min(list1)

"""
print(sys.argv)
print(*list, sep='\n')
"""



print("Min: ", min(list1))
print("Max: ", max(list1))
print("Mean: ", mean)
print("Median: ", median)
'''
print("Mode: ", mode)
'''
print("Range: ", rangee)

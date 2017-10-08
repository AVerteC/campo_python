#!usr/bin/env python3
import sys
inputs = sys.argv

inputs.remove('4204_arr.py')
inputs = list(map(int, inputs))

list1 = inputs
mean = sum(list1)/len(list1)



if (len(list1) % 2 == 0):
    list1.sort()
    mathan = int(len(list1)/2)-1
    mathas = len(list1)/2
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
print("Range: ", rangee)

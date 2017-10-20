#!/usr/bin/env python3
import sys

a =

quotient = float(sys.argv[2])/float(sys.argv[1])
remainder = int(sys.argv[2]) % int(sys.argv[1])

if (float(sys.argv[2]) % float(sys.argv[1]) )!= 0:
    remainder = float(remainder)


print("{} divided by {} equals {} remainder {}".format(sys.argv[2], sys.argv[1], quotient, remainder))

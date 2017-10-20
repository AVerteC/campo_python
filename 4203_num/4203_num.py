#!/usr/bin/env python3
import sys

a = 10
b = 56.99
c = 2+3j
d = 1234
typ = ""

quotient = float(sys.argv[2])/float(sys.argv[1])
quotient = round(quotient,4)
remainder = float(sys.argv[2]) % float(sys.argv[1])

if (float(sys.argv[2]) % float(sys.argv[1]) )!= 0:
    remainder = float(remainder)
    remainder = round(remainder, 4)
print("{} divided by {} equals {} remainder {}".format(sys.argv[2], sys.argv[1], quotient, remainder))





def typechecker(var):
    global typ
    check1 = (type(var) is int)
    check2 = (type(var) is float)
    check3 = (type(var) is complex)
    #long(x) are removed in python3 afaik
    #check4 = (type(var is long))

    if check1 == True:
        typ = typ + "int"
        return typ

    if check2 == True:
        typ = typ + "float"
        return typ

    if check3 == True:
        typ = typ + "complex"
        return typ



typechecker(a)
print("Variable a contains: {} which is of type {} ".format(a, typ))
typ = ""


typechecker(b)
print("Variable b contains: {} which is of type {} ".format(b, typ))
typ = ""

typechecker(c)
print("Variable c contains: {} which is of type {}".format(c, typ))
typ = ""

typechecker(d)
print("Variable d contains: {} which is of type {}".format(d, typ))
typ = ""

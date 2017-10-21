#!/usr/bin/env python3
import sys
#made by alan chen

# division segment
quotient = float(sys.argv[1])/float(sys.argv[2])
quotient = round(quotient,3)
remainder = float(sys.argv[1]) % float(sys.argv[2])

if (float(sys.argv[2]) % float(sys.argv[1]) )!= 0:
    remainder = float(remainder)
    remainder = round(remainder, 3)
print("{} divided by {} equals {} remainder {}".format(sys.argv[1], sys.argv[2], quotient, remainder))

#number typechecking/printing system

a = 10
b = 56.99
c = 2+3j
d = 1234
typ = ""



def typechecker(var):
    global typ
    global a
    global b
    global c
    global d
    check1 = (type(var) is int)
    check2 = (type(var) is float)
    check3 = (type(var) is complex)

    #long(x) are removed in python3 afaik
    #check4 = (type(var is long))
    if check1 == True:
        typ = ""
        typ = typ + "Integer"
        return typ

    if check2 == True:
        typ = ""
        typ = typ + "Float"
        return typ

    if check3 == True:
        typ = ""
        typ = typ + "Complex"
        var = str(var)
        var = var.replace("j","i").replace("(","").replace(")","")


        return typ







typechecker(a)
print("Variable a contains: {} which is of type: {} ".format(a, typ))
typ = ""


typechecker(b)
print("Variable b contains: {} which is of type: {} ".format(b, typ))
typ = ""

typechecker(c)
print("Variable c contains: {} which is of type: {}".format(c, typ))
typ = ""

typechecker(d)
print("Variable d contains: {} which is of type: {}".format(d, typ))

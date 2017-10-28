#!/usr/bin/env python3
import sys
#made by alan chen

# division segment

#number typechecking/printing system

a = 10
b = 56.99
c = 2+3j
d = 1234

def divnmod():
    quotient = float(sys.argv[1])/float(sys.argv[2])
    quotient = round(quotient,3)
    remainder = float(sys.argv[1]) % float(sys.argv[2])

    if (float(sys.argv[2]) % float(sys.argv[1]) )!= 0:
        remainder = float(remainder)
        remainder = round(remainder, 3)
        print("{} divided by {} equals {} remainder {}".format(sys.argv[1], sys.argv[2], quotient, remainder))


def typechecker(var):
    global dicta
    global typ
    typ = ""
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
        var = str(var)
        typ = typ + "Integer"
        dicta = {"Value":var, "Type":typ}
        return dicta

    if check2 == True:

        typ = ""
        var = str(var)
        typ = typ + "Float"
        dicta = {"Value":var, "Type":typ}
        return dicta

    if check3 == True:

        typ = typ + "Complex"
        var = str(var)
        var = var.replace("j","i").replace("(","").replace(")","")
        dicta = {"Value":var, "Type":typ}
        return dicta




def checka():
    global typ
    typechecker(a)
    global dicta
    print("Variable a contains: {} which is of type: {} ".format(dicta['Value'], dicta["Type"]))

def checkb():
    global typ
    typechecker(b)
    global dicta
    print("Variable b contains: {} which is of type: {} ".format(dicta['Value'], dicta["Type"]))

def checkc():
    global typ
    typechecker(c)
    global dicta
    print("Variable c contains: {} which is of type: {} ".format(dicta['Value'], dicta["Type"]))

def checkd():
    global typ
    typechecker(d)
    global dicta
    print("Variable d contains: {} which is of type: {} ".format(dicta['Value'], dicta["Type"]))

def main():
    divnmod()
    checka()
    checkb()
    checkc()
    checkd()

main()

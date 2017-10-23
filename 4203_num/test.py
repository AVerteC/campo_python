import sys

a = 2+3j

#print(type(a))


def typechecker(var):
    global typ
    check3 = (type(var) is complex)
    typ = ""
    if check3 == True:
        typ = typ + "Complex"
        var = str(var)
        var = var.replace("j","i").replace("(","").replace(")","")
        global dicta
        dicta = {"Value":var, "Type":typ}
        return dicta

def acheck():
    global typ
    typechecker(a)
    global dicta
    print("Variable a contains: {} which is of type: {} ".format(dicta['Value'], dicta["Type"]))



def main():
    acheck()


main()

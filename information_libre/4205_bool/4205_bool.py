#!usr/bin/env python3
# made by alan chen, intra id : ado


def arylogic():
    a1 = [False,True,True,None,True,None,None,False,False,None,True,False]
    a2 = ["or","or","or","==","!=","==","and","==","!=","and","!=","and"]
    a3 =[False,False,None,None,True,True,False,True,None,False,True,None]
    for i in range(len(a1)):
        print(str(a1[i])+ " " + a2[i] + " " + str(a3[i]), end = "  => ")
        print(eval(str(a1[i])+ " " + a2[i] + " " + str(a3[i])))
    # iterate through 3 arrays simultaneously, while evaluating them


def main():
    arylogic()


main()

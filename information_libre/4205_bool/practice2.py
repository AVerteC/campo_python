#!usr/bin/env python3
# made by Alan Chen

def arylogic():
    a1 = [1, 3]
    a2 = ["+", "-"]
    a3 =[2, 7]
    for i in range(len(a1)):
        print(str(a1[i])+ " " + a2[i] + " " + str(a3[i]), end = "  => ")
        print(eval(str(a1[i])+ " " + a2[i] + " " + str(a3[i])))
        # iterating through 3 arrays at the same time using range() to get var i to become a number

def main():
    arylogic()


main()

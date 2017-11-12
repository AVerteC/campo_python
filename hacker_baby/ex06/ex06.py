#!usr/bin/env python3
# made by alan chen

import sys


def gateinput():
    if len(sys.argv) == 1:
        print("No input detected")
        exit()
    else:
        if sys.argv[1].isnumeric() is True:
            if int(sys.argv[1]) < 1:
                print("\n")
                exit()
            else:
                cdn = int(sys.argv[1])
                return cdn
        else:
            print("\n")
            exit()


def d2b(cdn):
        if cdn <= 1:
            #print("a" + str(cdn))
            return str(cdn)
        else:
            #print(str(cdn//2)+" "+str(cdn % 2))
            return d2b(cdn//2)+str(cdn % 2)

def main():
    b = gateinput()
    #print(b)
    a = d2b(b)
    print(a)


main()

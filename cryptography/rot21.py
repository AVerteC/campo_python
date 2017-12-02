#!/usr/bin/env python3
# Made by Alan Chen

import sys


def pipecleaner():
    inputtext = ' '.join(sys.argv[1:])
    inputtext = inputtext.replace("[", "")
    inputtext = inputtext.replace("]", "")
    inputtext = inputtext.replace("\"", "")
    inputtext = inputtext.replace("", "")
    inputtext = inputtext.replace("\\n", "")
    return inputtext


def upperbet(c,rot):
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
    letterindex = uppercase.index(c) + rot
    if letterindex > 25:
        letterindex = letterindex % 26
        print(uppercase[letterindex], end="")


def lowerbet(c,rot):
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
    letterindex = lowercase.index(c) + rot
    if letterindex > 25:
        letterindex = letterindex % 26
        print(lowercase[letterindex], end="")
        
def crot(inputtext):

    for c in inputtext:
        if c.isupper():
            if c in uppercase:
                    letterindex = uppercase.index(c) + x
                    if letterindex > 25:
                        letterindex = letterindex % 26
                        print(uppercase[letterindex], end="")
                    else:
                        print(uppercase[letterindex], end="")
        elif c.islower():
            if c in lowercase:
                    letterindex = lowercase.index(c) + x
                    if letterindex > 25:
                        letterindex = letterindex % 26
                        print(lowercase[letterindex], end="")
                    else:
                        print(lowercase[letterindex], end="")
        else:
            print(c, end="")



def main():
    crot(pipecleaner())


main()

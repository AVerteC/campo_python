#!/usr/bin/env python3
# Made by Alan Chen

import sys


def pipecleaner():
    if len(sys.argv) != 2:
        print("")
        inputtext = ""
        return inputtext
    else:
        inputtext = ' '.join(sys.argv[1:])
        inputtext = inputtext.replace("[", "")
        inputtext = inputtext.replace("]", "")
        inputtext = inputtext.replace("\"", "")
        inputtext = inputtext.replace("", "")
        inputtext = inputtext.replace("\\n", "")
        return inputtext


def upperbet(c, rot):
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
    letterindex = uppercase.index(c) + rot
    letterindex = letterindex % 26
    print(uppercase[letterindex], end="")


def lowerbet(c, rot):
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
    letterindex = lowercase.index(c) + rot
    letterindex = letterindex % 26
    print(lowercase[letterindex], end="")


def crot(inputtext, rot):
    for c in inputtext:
        if c.isupper():
            upperbet(c, rot)
        elif c.islower():
            lowerbet(c, rot)
        else:
            print(c, end="")


def main():
    crot(pipecleaner(), 21)




main()

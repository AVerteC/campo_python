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


def upperconvert(c):
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
    upperconv = "•☋☀✇°☄♉⚆º✡☢☍☪☻¨☼⚉☌⚇⚬☉☾☽☪☊◆"
    print(upperconv[uppercase.index(c)], end="")


def lowerconvert(c):
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
    lowerconv = "¤«✹⌘†✠☯☸♌‡○~✆❄♒❖–—¬⟡*☺☹✞⧫"
    print(lowerconv[lowercase.index(c)], end="")


def wconv(inputtext):
    for c in inputtext:
        if c.isupper():
            upperconvert(c)
        elif c.islower():
            lowerconvert(c)
        else:
            print(c, end="")


def main():
    wconv(pipecleaner())


main()

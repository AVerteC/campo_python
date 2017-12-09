#!/usr/bin/python3
# Made by Alan Chen

import sys

def cleaner(text):
    text = text.replace("[", "")
    text = text.replace("]", "")
    text = text.replace("\"", "")
    text = text.replace("", "")
    text = text.replace("\\n", "")
    print(str(text))
    return text


def alphaindex(text):
    index = []
    indexposition = 0
    for c in text:
        if c.isupper():
            upperkbet(c, kindexposition, kindex)
            kindexposition += 1
        elif c.islower():
            c = c.upper()
            upperkbet(c, kindexposition, kindex)
            kindexposition += 1

            # should be enabled for punctuation in key?
            # punctuation marks do not have alphavalues
            # else:
            #    kindex.insert(kindexposition, c)
            #    kindexposition += 1

    #make the key all uppercase


    print(kindex)
    return kindex

def tindexlogic(inputtext):
    tindex = []
    tindexposition = 0
    for c in inputtext:
        if c.isupper():
            uppertbet(c, tindexposition, tindex)
            tindexposition += 1
        elif c.islower():
            lowertbet(c, tindexposition, tindex)
            tindexposition += 1
        else:
            tindex.insert(tindexposition, c)
            tindexposition += 1

    print(tindex)
    return tindex
'''
def vignerecalc(kindex,tindex):
    for v in tindex:
'''


def upperkbet(c, kindexposition, kindex):
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
    letterindex = uppercase.index(c)
    letterindex = letterindex % 26
    kindex.insert(kindexposition, letterindex)

def uppertbet(c, tindexposition, tindex):
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
    letterindex = uppercase.index(c)
    letterindex = letterindex % 26
    tindex.insert(tindexposition, letterindex)


def lowertbet(c, tindexposition, tindex):
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
    letterindex = lowercase.index(c)
    letterindex = letterindex % 26
    tindex.insert(tindexposition, letterindex)


def main():
    kindex = kindexlogic(cleaner(sys.argv[1]))
    tindex = tindexlogic(cleaner(sys.argv[2]))
    # vignerecalc(kindex, tindex)


main()


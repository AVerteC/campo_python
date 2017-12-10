#!/usr/bin/python3
# Made by Alan Chen

import sys


def cleaner(text):
    text = text.replace("[", "")
    text = text.replace("]", "")
    text = text.replace("\"", "")
    text = text.replace("", "")
    text = text.replace("\\n", "")
    return text


def alphaindex(text):
    index = []
    indexpos = 0
    for c in text:
        if c.isupper():
            aindex(c, indexpos, index)
            indexpos += 1
        elif c.islower():
            c = c.upper()
            aindex(c, indexpos, index)
            indexpos += 1
        else:
            print("error")
    return index




def vignerencrypt(kindex,tindex):
    pos = 0
    klen = len(kindex)
    kpos = 0
    out = ""
    #print(tindex)
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    for v in tindex:
        #print(v)
        kpos = (pos % klen)
        v = v + kindex[kpos]
        v = v % 26
        letter = str(lowercase[v])#+1])
        #print(letter)
        pos += 1
        kpos += 1
        out = out + letter
    print(out)

def aindex(c, indexpos, index):
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
    letterindex = uppercase.index(c)
    letterindex = letterindex % 26
    index.insert(indexpos, letterindex)


def main():
    kindex = alphaindex(cleaner(sys.argv[1]))
    tindex = alphaindex(cleaner(sys.argv[2]))
    vignerencrypt(kindex, tindex)


main()


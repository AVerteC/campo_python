#!/usr/bin/python3
# Made by Alan Chen

import sys


def cleaner(text):
    # print(text)
    text = text.replace("[", "")
    text = text.replace("]", "")
    text = text.replace("\"", "")
    text = text.replace("", "")
    text = text.replace("\\n", "")
    # print(text)
    return text


def alphaindex(text):
    index = []
    indexpos = 0
    for c in text:
        if c.isupper():
            aindex(c+'A', indexpos, index)
            indexpos += 1
        elif c.islower():
            c = c.upper()
            aindex(c, indexpos, index)
            indexpos += 1
        else:
            index.insert(indexpos, c)
            indexpos += 1
    # print(index)
    return index




def vignerencrypt(kindex,tindex):
    pos = 0
    klen = len(kindex)
    kpos = 0
    out = ""
    #print(tindex)
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    for v in tindex:
        if 'A' in str(v):
            #print(v)
            v = v[0:len(v) - 1]
            #print(v)
            v = int(v)
            kpos = (pos % klen)
            v = v + kindex[kpos]
            v = v % 26
            letter = str(lowercase[v])
            letter = letter.upper()
            # print(letter)
            pos += 1
            kpos += 1
            out = out + letter
        # current thought: remove A from the value and the uppercase the letter output.
        elif str(v).isdigit():
            # print(v)
            kpos = (pos % klen)
            v = v + kindex[kpos]
            v = v % 26
            letter = str(lowercase[v])
            # print(letter)
            pos += 1
            kpos += 1
            out = out + letter
        else:
            out = out + v

    print(out)


def aindex(c, indexpos, index):
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
    if len(c) == 2:
        c = c[0]
        # print(c)
        letterindex = uppercase.index(c)
        letterindex = letterindex % 26
        letterindex = str(letterindex) + 'A'
        # print(letterindex)
        index.insert(indexpos, letterindex)
        # print(index)
    else:
        letterindex = uppercase.index(c)
        letterindex = letterindex % 26
        index.insert(indexpos, letterindex)
    # print(index)

def main():
    # print(sys.argv[2])
    kindex = alphaindex(cleaner(sys.argv[1]))
    tindex = alphaindex(cleaner(sys.argv[2]))
    vignerencrypt(kindex, tindex)


main()


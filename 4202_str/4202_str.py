#!/usr/bin/env python3
import sys
import re
#inputs = 'abcdefghijklmnopqrstuvwxyz'


def eol_cap(s):
    cap = [False]
    def repl(m):
        cap[0] = not cap[0]
        return m.group(0).upper() if cap[0] else m.group(0).lower()
    return re.sub(r'[A-Za-z]', repl, s)

print(eol_cap(sys.argv[1]))

def eol_noncap(s):
    cap = [False]
    def inv_repl(m):
        cap[0] = not cap[0]
        return m.group(0).replace(,"*") if m.group(0).upper() else cap[0]
    return re.sub(r'[A-Za-z]', repl, s)

nexinput = eol_cap(sys.argv[1])
#def iterate_chars(word):
#    for i in range(2, len(word)):
#        print(word[i])

#iterate_chars(str)

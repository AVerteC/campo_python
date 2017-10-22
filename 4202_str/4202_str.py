#!/usr/bin/env python3
import sys
import re
#inputs = 'abcdefghijklmnopqrstuvwxyz'
#made by alan chen
#print(sys.argv[1][0])
#print(sys.argv[1][1:])

fl = sys.argv[1][0]
rest = sys.argv[1][1:]

def eol_cap(s):
    cap = [False]
    def repl(m):
        cap[0] = not cap[0]
        return m.group(0).upper() if cap[0] else m.group(0).lower()
    return re.sub(r'[A-Za-z]', repl, s)

def eol_noncap(s):
    return re.sub(r'[AEIOU]', "*", s)

def line_removenp(s):
    return re.sub(r'[^()]', "", s)
"""
def check_parentheses(s):
    Lmath = ""
    Rmath = ""
    for i in range(len(s)):
        if i = "(":
            Lmath = 1
        if i =
"""
stage1 = sys.argv[1][0] + eol_cap(sys.argv[1][1:])
stage2 = eol_noncap(stage1)
stage3 = line_removenp(stage2)



print(stage1)
print(stage2)
print(stage3)

#check_parentheses(stage3)

#def iterate_chars(word):
#    for i in range(2, len(word)):
#        print(word[i])

#iterate_chars(str)

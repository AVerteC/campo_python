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

def check_parentheses(s):
    #total parentheses value
    mtotal = 0
    for c in s:
        if c == "(":
            mtotal += 1
        if c == ")":
            mtotal -= 1

    #block failure state of )(
        if mtotal < 0:
            print("Balanced? False")
            return
    #pass
    if mtotal == 0:
        print("Balanced? True")
    #fail
    else:
        print("Balanced? False")

#split the string after the first character ex. "Help!" => "H" "elp!"
#and then capitalize the second part
stage1 = sys.argv[1][0] + eol_cap(sys.argv[1][1:])

#change all vowels to "*"
stage2 = eol_noncap(stage1)

#remove all characters except parentheses
stage3 = line_removenp(stage2)



print(stage1)
print(stage2)

#print(stage3)

#check the parenteses balance
check_parentheses(stage3)

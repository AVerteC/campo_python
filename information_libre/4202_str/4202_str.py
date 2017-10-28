#!/usr/bin/env python3
import sys
import re
#made by alan chen

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
def s1():
    global stage1
    stage1 = sys.argv[1][0] + eol_cap(sys.argv[1][1:])
    print(stage1)

def s2():
#change all vowels to "*"
    global stage2
    stage2 = eol_noncap(stage1)
    print(stage2)

def s3():
#remove all characters except parentheses
    global stage
    stage3 = line_removenp(stage2)
    check_parentheses(stage3)




def main():
    s1()
    s2()
    s3()

main()

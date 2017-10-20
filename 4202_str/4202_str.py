#!/usr/bin/env python3
str = "abcdefghijklmnopqrstuvwxyz"


def iterate_chars(word):
    for i in range(2, len(word)):
        print(word[i])

iterate_chars(str)

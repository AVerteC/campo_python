#!/usr/bin/env python3
# made by Alan Chen
# use python3


def practiceinput():
        addon = "ahah"
        word = input("Please input a word: ")
        # string interpolation with .format
        print(word + " {0}".format(addon))


def main():
    practiceinput()


main()

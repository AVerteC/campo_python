#!/usr/bin/env python3
#made by alan chen


def getfileLines():
    file = open("names.txt", "r")
    allLines = file.readlines()
    return allLines
    # testing the file reading output

def main():
    print(getfileLines())


main()
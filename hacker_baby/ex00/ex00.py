#!/usr/bin/env python3


def name():
    print("Hello hacker, what is your name?")
    name = input("")
    print("Welcome, {0}.".format(str(name)))


def main():
    name()

main()
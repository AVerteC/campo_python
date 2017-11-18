#!/usr/bin/env python3
# made by alan chen, intra id : ado
# mad libs program usin argv !
# use python3
import sys


def madlibs():

    if len(sys.argv) == 2:
        Title = sys.argv[1].upper()

        adjective = input("Please input an adjective: ")
        business = input("Please input a business: ")
        animal = input("Please input an animal: ")
        noise = input("Please input a noise: ")

        print('\n' + Title)
        # print(Title)

        print('{0} MacDonald had a {1}, E-I-E-I-O \n'
        'and on that {2} he had a {3}, E-I-E-I-O \n'
        'with a {4} {5} here \n'
        'with a {6} {7} there, \n'
        'here a {8}, there a {9}, \n'
        'everywhere a {10} {11}, \n'
        '{12} MacDonald had a {13}, E-I-E-I-O!'
        .format(adjective, business, business, animal, noise, noise, noise, noise, noise, noise, noise, noise, adjective, business))

    else:
        print('title not detected')


def main():
    madlibs()


main()

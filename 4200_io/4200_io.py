#!/usr/bin/env python3
#made by alan chen
#mad libs program usin argv !
#use python3
import sys


def madlibs():

    if len(sys.argv) == 2:
        Title = sys.argv[1].upper()

        adjective = input("Please input an adjective: ")
        business = input("Please input a business: ")
        animal = input("Please input an animal: ")
        noise = input("Please input a noise: ")

        print('\n' + Title)
        #print(Title)

        print('{0} MacDonald had a {1}, E-I-E-I-O \n'
        'and on that {2} he had a {3}, E-I-E-I-O \n'
        'with a {4} {5} here \n'
        'with a {6} {7} there, \n'
        'everywhere a {8} {9}, \n'
        '{10} MacDonald had a {11}, E-I-E-I-O!'
        .format(adjective, business, business, animal, noise, noise, noise, noise, noise, noise, adjective, business))

    else:
        print('title not detected')

def main():
    madlibs()



main()
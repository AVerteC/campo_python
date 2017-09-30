#!/usr/bin/env python
#mad libs program usin argv !
#use python3
import sys




if len(sys.argv) == 2:
    Title = sys.argv[1].upper()

    adjective = input("Please input an adjective: ")
    business = input("Please input a business: ")
    animal = input("Please input an animal: ")
    noise = input("Please input a noise: ")

    print('\n')
    print(Title)

    print('%s MacDonald had a %s, E-I-E-I-O \n'
    'and on that %s he had a %s, E-I-E-I-O \n'
    'with a %s %s here \n'
    'with a %s %s there, \n'
    'everywhere a %s %s, \n'
    '%s MacDonald had a %s, E-I-E-I-O!'
    ) % (adjective, business, business, animal, noise, noise, noise, noise, noise, noise, adjective, business)

else:
    print('title not detected')

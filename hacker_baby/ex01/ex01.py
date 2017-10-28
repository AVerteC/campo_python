#!/usr/bin/env python3

def interrogation():
    print("Who goes there?")
    name = input('')

    if name == 'DHTFHNUQARFMQMKGSPRLRSKBCMD':
        print("Welcome Daenerys.")
    else:
        print('Move along, now')

    if name == 'Dany':
        print('Dany who?')

def main():
    interrogation()

main()
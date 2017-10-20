#!/usr/bin/env python3

secret = "memes"

print("The secret word begins with a D.")
gueso = 0


for x in range(0,11):

    guess = input('GUESS: ')
"""print (len(guess))"""
    """print ("Debuga {} guess".format(gueso))
    """

    if len(guess) != 0 & len(guess) < 5   :
        print("0, 1, 2, 3, 4 that's how we count to five!")
        gueso += 1





    if len(guess) == 0:
        print("You wasted a guess =P")
        gueso += 1


    if guess[:1] !='m' and len(guess) == 5:
        print("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        gueso += 1


    if guess[:1] =='m' and len(guess) == 5 and guess != "memes":
        print("You have {} guesses left".format(gueso))
        gueso += 1


    if guess == "memes":
        print("Good Job! You are one with the Source.")
        quit()

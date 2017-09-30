#!/usr/bin/env python3

secret = "memes"

print("The word starts with the letter m, Please guess a five letter word.")

for x in range(0,11):

    guess = input('Your guess: ')


    if len(guess) < 4 and :
        print("0, 1, 2, 3, 4 that's how we count to five!")

    if len(guess) == 0:
        print("You wasted a guess =P")

    if guess[:1] !='m' and len(guess) == 5:
        print("abcdefghijklmnopqrstuvwxyz")

    if guess[:1] =='m' and len(guess) == 5 and guess != "memes":
        print("You have" x "guesses left")

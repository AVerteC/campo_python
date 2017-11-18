#!/usr/bin/env python3
# made by alan chen, intra id : ado


def guessinggame():

    print("The secret word begins with a m.")
    gueso = 9

    for x in range(1, 11):

        guess = input('GUESS: ')
        # print (len(guess))"""
        # print ("Debuga {} guess".format(gueso))

        if len(guess) > 0 and len(guess) < 4:
            print("0, 1, 2, 3, 4 that's how we count to five!")
            gueso -= 1

        elif len(guess) == 0:
            print("You wasted a guess =P")
            gueso -= 1

        elif guess[:1] != 'm' and len(guess) == 5:
            print("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            gueso -= 1

        elif guess[:1] == 'm' and len(guess) == 5 and guess != "memes":
            print("You have {} guesses left!".format(gueso))
            gueso -= 1

        elif guess == "memes":
            print("Good Job! You are one with the Source.")
            quit()


def main():
    guessinggame()


main()

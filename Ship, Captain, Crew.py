# File name: Ship, Captain, Crew.py
# Author name: Kali Hale
# Date: 11-10-19
# Description: This program automates and simulates the dice rolls for Ship, Captain, Crew, also known as 4-5-6

import random

class dice:
    def __init__(self):
        self.dice = [0]*5
        self.rollall()
        self.score = 0

    def roll(self, which):
        for pos in which:
            self.dice[pos] = random.randrange(1, 7)

    def rollall(self):
        self.roll(range(5))

    def rollwhich(self):
        countsixes, setofsixes = self.search(6)
        countfives, setoffives = self.search(5)
        countfours, setoffours = self.search(4)
        countthrees, setofthrees = self.search(3)
        counttwos, setoftwos = self.search(2)
        countones, setofones = self.search(1)
        if countsixes >= 1:
            setofsixes.pop(0)
            if countfives >= 1:
                setoffives.pop(0)
        if countsixes >= 1 and countfives >= 1:
            if countfours >= 1:
                setoffours.pop(0)
        self.roll(setofsixes)
        self.roll(setoffives)
        self.roll(setoffours)
        self.roll(setofthrees)
        self.roll(setoftwos)
        self.roll(setofones)

    def values(self):
        print("Your dice values are", self.dice)
        return self.dice[:]

    def roundscore(self):
        countsixes, setofsixes = self.search(6)
        countfives, setoffives = self.search(5)
        countfours, setoffours = self.search(4)
        countthrees, setofthrees = self.search(3)
        counttwos, setoftwos = self.search(2)
        countones, setofones = self.search(1)
        if countsixes > 0 and countfives > 0 and countfours > 0:
            rollscore = ((countsixes - 1) * 6) + ((countfives - 1) * 5) + ((countfours - 1) * 4) + (countthrees * 3) + \
                        (counttwos * 2) + (countones * 1)
        else:
            rollscore = 0
        return rollscore

    def totalscore(self):
        self.score = self.score + self.roundscore()
        return self.score

    def search(self, find):
        number = 0
        setof = []
        for i in range(len(self.dice)):
            if self.dice[i] == find:
                number = number + 1
                setof.append(i)
            else:
                continue
        return number, setof

    def shipcaptainorcrew(self):
        countsixes, setofsixes = self.search(6)
        countfives, setoffives = self.search(5)
        countfours, setoffours = self.search(4)
        if countsixes >= 1 and countfives == 0 and countfours == 0:
            print("You have your ship!")
        elif countsixes >= 1 and countfives >= 1 and countfours == 0:
            print("You have your ship and your captain!")
        elif countsixes >= 1 and countfives >= 1 and countfours >= 1:
            print("You have your ship, your captain, and your crew!")


def printintro():
    print("Welcome to Ship, Captain, Crew!")
    print("Here's how the rules go: Each player gets three rolls. If you get a 6, that's your ship. If you get a \n"
          "5, that's your captain. If you get a 4, that's your crew. But you have to get them in order. If you get \n"
          "a roll with a 5 and no 6s, you have to reroll everything. The same goes for if you get a 4 without a 5 - \n"
          "unfortunately, you'll have to reroll that 4. Once you have a ship, a captain, and a crew,\n"
          "that's when you begin to earn points.\n"
          "Points are calculated by adding the values of the last two dice in the set once you get a ship, a captain,\n"
          "and a crew, and you'll earn points from those two dice during your remaining rerolls if you still have any."
          "\n\n"
          "Ordinarily you would have to choose which dice to reroll yourself, but this program automates it. All you \n"
          "have to do is play and have fun!")
    print()


def getnames():
    player1 = input("Enter the name of player 1: ")
    player2 = input("Enter the name of player 2: ")
    return player1, player2


def main():
    printintro()
    player1, player2 = getnames()
    p1dice = dice()
    p2dice = dice()

    for i in range(0, 3):
        print()
        print()
        print("Round ", (i+1))
        print()
        print("Player 1: ", player1)
        p1dice.values()
        p1dice.shipcaptainorcrew()
        p1score = p1dice.totalscore()
        print(player1, "'s score is ", p1score)

        print()
        print("Player 2: ", player2)
        p2dice.values()
        p2dice.shipcaptainorcrew()
        p2score = p2dice.totalscore()
        print(player2, "'s score is ", p2score)

        if i < 2:
            emergencyexit = input("Ready to roll to continue? Press enter to roll again or enter 'q' to quit: ")

            if emergencyexit == "q":
                break
            else:
                p1dice.rollwhich()
                p2dice.rollwhich()
        elif i == 2:
            if p1score > p2score:
                print(player1, " wins!")
            elif p2score > p1score:
                print(player2, " wins!")
            else:
                print("It's a tie!")

    print("Thanks for playing Ship, Captain, Crew!")


main()

# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.
import random
randunNumber = 8
def roll_die():
    die1 = random.randint(1, randunNumber)
    die2 = random.randint(1, randunNumber)
    total = die1 + die2
    print("Die 1: roll die", die1)
    print("Die 2: roll die", die2)
    print("Total value: roll die", total)
   
def roll_die2() :
    die1 = 10
    print("Die 1 rolldie 2:", die1)
    roll_die()
    roll_die()
    roll_die()
    print("Die 1 roll die2:", die1)
roll_die2()
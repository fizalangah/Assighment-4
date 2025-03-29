# Simulate rolling two dice, and prints results of each roll as well as the total.


import random
diceNumber = 6
def roll_die():
    die1 = random.randint(1, diceNumber)
    die2 = random.randint(1, diceNumber)
    total = die1 + die2
    print("Die 1: roll die", die1)
    print("Die 2: roll die", die2)
    print("Total value: roll die", total)
roll_die()   
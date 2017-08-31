#
# Write a simple program that, when run, prompts the user for input then prints a result.
#
# Program should ask the user for the number of dice they want to roll as well as the number of sides per die.
#
# 1. Open Atom
# 1. Create a new file and save it as `dice.py`
# 1. Follow along with your instructor
#
#
# 1. [Compound statements](https://docs.python.org/3/reference/compound_stmts.html)
# 1. [Python Std. Library: Random Module random.randint()](https://docs.python.org/3/library/random.html#random.randint)
#
#
# - Importing
# - The Random Module
# - `for` looping
# - `input()` function
# - programmatic logic

from random import randint

# roll=input("Press Y to roll the dice, press N to quit. ")
# x=0
# while roll.lower()=='y':
#     x=int(input("Number of dice side: "))
#     y=int(input("Number of rolls: "))
#     print(randint(1,x))
#     roll = input("Press Y to roll again, N to quit. ")
#
# print("Okay, we'll put the dice away.")


user_dice_roll = int(input("Number of dice you want to roll: "))
die_side = int(input("Number of sides per dice:  "))


for i in range (1, user_dice_roll+1):
    print('Roll Number:',*(i), 'Dice No.',(randint(1, die_side)))

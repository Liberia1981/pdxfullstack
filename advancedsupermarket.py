"""
Lab: Change Return

Delivery Method: Doctests

Goal

Write a python script that figures out how to divvy up an amount of change into the _fewest_ quarters, dimes, nickels, and pennies.

Instructions

Some supermarkets have automatic change dispensers.

*   Ask for the amount of change to dispense _in cents_.
    Assume that the amount input will be less than 100 cents.

*   Calculate the number of quarters necessary first.

*   Then calculate the number of dimes, nickels, and pennies.
    If you do it in that order, you will minimize the number of coins.

This is easiest done by updating a _running total_ of number of cents left to be put into coins.

Also remember that the `//` operator divides and removes any remainder.

Documentation

Advanced

Expand this problem to work on an amount of cents greater than 100 and include bills.
Print out the total number of coins and bills dispensed.
"""
user = int(input("Type the amount of change to dispense in cents? "))
franklin = 100
grant = 50
Jackson = 20
hamilton = 10
lincoln = 5
washington = 1
quarter = .25
dime = .10
nickel = .5
penny = .1
a = user//quarter
b = user%quarter
a = user//quarter
b = user%quarter
c = b//dime
d = b%dime
e = d//nickel
f = d%nickel


print('You have {} quarter(s), {} dime(s), {} nickel(s), and {} penny/pennies '.format(a, c, e, f))

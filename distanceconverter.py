# Lab: Distance Converter

#Delivery Method: Prompt Only

# Goal

# Write a function to convert between `mi`, `km`, `ft`, and `m`.

# Instructions

# Ask the user for a distance, then the units of that distance, then the target units.
# Then print out the conversion as below.

# > Enter a distance:
# > 100
# > Enter units:
# > mi
# > Enter target units:
# > km
# > 100 mi is 160.93440000000115 km

# Support converting between `mi`, `km`, `ft`, and `m`.

# Documentation

# 1. [Python Official: Built-In Functions](https://docs.python.org/3.6/library/functions.html)
#
# 1. [Python Official: Operators](https://docs.python.org/3.6/library/operator.html#mapping-operators-to-functions)
#1. have person pick the unit they want to convert
#2. have person pick the unit they want to convert to
#3. write the function for converting one unit to another
def display_message():
    print("=============================")
    print("****   DISTANCE CONVERTER   ****")
    print("=============================")
    print("PICK THE UNIT YOU DESIRE TO CONVERT")
    print("=============================")
    print("1 FOR MILE, 2 FOR KILOMETER, 3 FOOT AND 4 FOR METER")
    print("=============================")
display_message()
user_from = int(input("Unit you will convert: "))

def _unitpick_(x):
    distance = ["Mile", "Kilometer","Foot","Meters",]
    unit_from=distance[x-1]
    if unit_from==str("Miles"):
        print(unit_from)
    elif unit_from==str("Kilometer"):
        print(unit_from)
    elif unit_from==str("Feet"):
        print(unit_from)
    elif unit_from==str("Meters"):
        print(unit_from)
    else:
        print(unit_from)
    print('Converting from:',unit_from)
    return(unit_from)
_unitpick_(user_from)

user_number=int(input("Input number of you like to convert from: "))

user_to=int(input("Unit you will convert to: "))
def _unitconvertto_(x):
    distance = ["Mile", "Kilometer","Foot","Meters",]
    unit_to=distance[x-1]
    print('Converting to:', unit_to)
    return(unit_to)
_unitconvertto_(user_to)
# def whatisit():
#     unit_to=whatisit()
#     print(unit_to,"confusing bull shit")
# whatisit(_unitpick_):


def _miles(x):
    conversion=unit_to
    if conversion=='Kilometer':
        return miles*1.61
    elif Conversion=='Feet':
        return miles*5280
    elif conversion=='Meters':
        return miles*1609.34
    else:
        _miles(x)
_miles(user_number)

#
#
# def _kilometer_():
#     kilometers_to_miles=x*0.62
#     kilometers_to_feet=x*3280.84
#     kilometers_to_meters=x*1000
# def _feet_():
#     feet_to_miles=x*0.00019
#     feet_to_kilometers=x*0.00030
#     feet_to_meters=x*0.305
# def _meter_():
#     meters_to_miles=x*0.00062
#     meters_to_kilometers=x*0.001
#     meters_to_feet=x*3.281
# Advanced

#Also support converting between `in` and `cm`.

# Also support converting between `gal` and `L`.
# Error if someone tries to convert between volume and distance. Use `raise`.

# Super Advanced

# * Also support converting between all [metric prefixes](https://en.wikipedia.org/wiki/Metric_prefix) of meters.

# Key Concepts

# - Variables
# - Function definition
# - User input
# - Built-In functions
# - Logic Problems

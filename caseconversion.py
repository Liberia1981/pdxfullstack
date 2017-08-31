# # Lab: Case Conversion
#
# ###### Delivery Method: Doctests
#
# ##### Goal
#
# Write a program that prompts the user for a word.
# Print out either  `snake_case` or `CamelCase` depending case convention it is!.
#
# --------------------
#
# ##### Instructions
#
# Use substring membership with the `in` operator
#
# -------------------
# #### Documentation
#
# 1. [PEP8](https://www.python.org/dev/peps/pep-0008/)
# 1. [Stack Overflow](http://stackoverflow.com/questions/159720/what-is-the-naming-convention-in-python-for-variable-and-function-names)
#
# ---------------------
# #### Key Concepts:
#
# - Python social conventions for variable and function naming

word = input("Type in a word ")
def caseconversion(word):
    if word.islower() and '_' in word:
        print('snake_case')
    elif word[0].isupper() and not '_' in word:
        print('CamelCase')
    else:
        print('Try again sucka!!!')
        pass

x = True
while x == True:
    word = input("Type a word: ")
    caseconversion(word)
    if input("another word? y/n: ") == "n":
        x = False
    else:
        pass

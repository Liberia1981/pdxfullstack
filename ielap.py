# """
# Lab: I before E except after C.
#
# From wikipedia:
# The i before e except after c rule is not worth teaching. It applies only to words in which
# the ie or ei stands for a clear /ee/ sound and unless this is known, words such
# as 'sufficient', 'veil' and 'their' look like exceptions.
#
# ###### Delivery Method: Prompt
#
# ------------------------------
#
# #### Goal
#
# Create a program that asks for a _single_ English word and checks if it follows the
# rule **I before E except after C.**
#
#
# ---------------------------------------------------------
#
# #### Instructions
#
# 1. Create a file named `spelling.py`
# 1. Write a function that searches for the index of any instances of `ie` in the string,
# then see if the preceding letter is `c`.
#
#
# ------------------
#
#  Documentation
#
#  """

# The i before e except after c rule is not worth teaching. It applies only to words in which
# the ie or ei stands for a clear /ee/ sound and unless this is known, words such
# as 'sufficient', 'veil' and 'their' look like exceptions.



def ie_test(string):
    if "ie" in string:
        if "cie" in string:
            print("Does not follow rule.")
        elif 'cie' 
        else:
            print("you gave me an ie without a C")
    else:
        print("no ie")

x = True
while x == True:
    string = input("gimmie a string: ")
    ie_test(string)
    if input("another word? y/n: ") == "n":
        x = False
    else:
        pass

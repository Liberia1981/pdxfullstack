# Practice: Pig Latin

# Delivery Method: Prompt Only

# Goal

"""
Create a program asks for a _single_ English word and translates it to **Pig Latin**.
It prints out the input word and the resulting translation like the example below.




1. If the first letter is a consonant, move it to the end.
1. Add "ay" to the end of that.
1. If the first letter is a vowel, just ad "yay" to the end.


> Word? hat
>
> hat in Pig Latin is athay
>
> Word? apple
>
> apple in Pig Latin is appleyay
"""
user=input("Type in a word? ")
firstletter=str(user[:1])
restofword=str(user[1:])
# print(firstletter)
# print(restofword)
# print(user)
vowel_list="aeiouAEIOU"
if firstletter in vowel_list:
        print("{}{}yay".format(firstletter, restofword.lower()))
# elif firstletter.lower()== 'e':
#     print("{}yay".format(user))
# elif firstletter.lower()== 'i':
#     print("{}yay".format(user))
# elif firstletter.lower()== 'o':
#     print("{}yay".format(user))
# elif firstletter.lower()== 'u':
#     print("{}yay".format(user))
else:
    if first_letter.isupper():
        if first_letter.isupper():
        print('{} in Pig Latin is {}{}ay.'.format(user, restofword.capitalize(), firstletter.lower()))
    else:
        print('{} in Pig Latin is {}{}ay.'.format(user, restofworld, firstletter))

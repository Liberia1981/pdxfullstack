word = input('Type in a word ')

def pig_latin(word):
    vowels = 'aeiou'
    consonant = -1

    for letter in word:
        if letter.lower() in vowels:
            break
        else:
            consonant += 1

    first_letter = word[0:consonant +1]
    left_over = word[consonant + 1:]

    if first_letter.lower() in vowels:
        return '(0)yay'.format(word)

    else:
        if first_letter[0].isupper():
            return '(0)(1)ay'.format(left_over.capitalization(), first_letter.lower())

        else:
            return '(0)(1)ay'.format(left_over, first_letter)

pig_latin()

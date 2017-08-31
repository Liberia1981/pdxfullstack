#my_list = ['cat', 'dog', 'monkey']

#pets_string = ', '.join(my_list)

#text = "My pets are : {}.".format(pets_string)

#print(text)

#text = "My pets are : {}.".format(', '.join(my_list))

#print(text)

#my_list = ['cat', 'dog', 'monkey']

#my_list[1] = 'ferret'

#print(my_list)

#my_tuple=('cat', 'dog', 'monkey')
# cannot be moved like list....
#print(my_tuple)

#my_tuple=('cat', ['4', '5', '6'], 'monkey')
#can change list inside of tuple
#print(my_tuple)

my_list =['cat', 'dog', 'monkey']
#print(my_list)
#for pet in my_list:
    #print(pet)

#for pet in my_list:
    #for char in pet:
#        print(char)
#    print()

#while True:
#    print('This is the song that never ends...')

#num = 0
#while num < 100:
#    print('This is the song that never ends...', num)
#    num +=1
#print("Oh never mind. it's over")

#print(4==4 and 5==5)

#if orig_unit == 'mi':
#    if to_unit == 'km':
#        something = **miles to km math**
#    elif to_unit == 'in':
#        something = **miles to in math**

#if orig_unit == 'km':
#    if to_unit == 'mi':
#        something = **miles to km math**
#    elif to_unit == 'in':
#        something = **miles to in math**

# name = input('what is your name?: ')
#
# if name == 'Chris':
#     print('uh, hi {}'.format(name))
# elif name == "chelsea":
#     print('It\'s {}'.format(name))
# else:
#     print('Hello {}'.format(name))
#
# def my_function():
#     print('Coding is fun!')
# thing= my_function()
# thing()
#Piglatin --- classroom
# word = input("What word would you like translated?: ")
# # split first letter from word so we have two parts
# first_letter = word[0]
# left_over = word[1:]
# # list vowel_list
# vowels = 'aieouAEIOU'
name = 'Chris'
# {'key':'value'} ---- key and value  for dictionary.   value can be anything
# my_dict = {'key1': 'value1', 'key2': 'value2'}
# print(my_dict)
# print(my_dict['key1'])
# my_dict = {'key1': {'some': 'thing'}, 'key2': 'value2'}
#
# print(my_dict['key1']['some'])

# my_dict = {'key1': {'some': 'thing'}, 'key2': 'value2'}
# print(my_dict)
# my_dict['key3'] = 'value3'
# print(my_dict)
# my_dict['key3']  = 'value4'
# print(my_dict)
# print(my_dict.keys())
#print keys only
# my_dict = {'key1': ['some', 'thing'], 'key2': 'value2'}
#
# print(my_dict['key1'][1])

# students = {
#     'watters':{'name': 'Kasey Watters', 'phone': 3333333333},
#     'Magnuson':{'name': 'Tom Magnuson', 'phone': 4444444444},
#     'Yeaney': {'name': 'Johnny Yeaney', 'phone': 5555555555},
# }
#
# query = input('What is the last name of the person you are looking for? ')
#
# print(students[query]['name'])
# print(students[query]['phone'])

# def greeting(name):
#     return('Hello {}!'.format(name.capitalize()))
# text = greeting('johnny')
# print(text)
#
# def greeting(name, age=21):
#     return('Hello {},you are {}!'.format(name.capitalize(),age))
# text = greeting('johnny', 34)
# print(text)
# def greeting(name, age=21):
# def comes first, next is the name of the function(gretting), after that you will stat your
# argment'()'.   and lastly you will you ':' if you have conditionals after.
#     print(5*5)
#     return('Hello {},you are {}!'.format(name.capitalize(),age))
#     print('Johnny')
# text = greeting('johnny', 34)
# print(text)
#
# def add_things(*args):
#     # *args--- unknown amount of arguments-- as long as you have *
#     print(args)
# add_things(3,6,8,12,56347)
# def add_things(*args):
#     total = 0
#     for num in args:
#         total += num
#         return total
#
# print(add_things(3,6,8,12,56347))
#
# def add_things(*kwargs):
#     # *kwargs--- key word arguments*
#     print(kwargs)
# add_things({'I like Pie':  True})

# string = 'I like to eat pie!'
# def thing(x):
#     if x == 'i':
#         return True
#     else:
#         return False
#
# new_list = list(filter(thing, string))
# print(new_list)

# statement = 'I like to eat pie!'
# def filter_function(x):
#     if x == 'i':
#         return True
#     else:
#         return False
#
# new_list = list(filter(filter_function, statement))
# print(new_list)

# statement = 'I like to eat pie!'
# def filter_function(x):
#     return x == 'i':
#     #     return True
#     # else:
#     #     return False
#
# new_list = list(filter(filter_function, statement))
# print(new_list)

# for y in range(80, 101, 5,):
#     print(y)
#     print(y+0)

# fruit = ['apples', 'apples','orange']
# fruit_set = set(fruits)
# print(fruit_set)

# from random import randint as foo
#
# def randint (x, y):
#     print('sucka')
#
# print(foo(1, 2))
# word =int(input("Type in a number "))
# def _radius_sample_(radius):
#     area = 3.14 * radius * radius
#     print(area)
#
# _radius_sample_(word)
# print(ran)
# ran += 1
# try:
#     q = int(input('press 1 to continue press 2 to exit: '))
# except:
#     print('I don\'t understand what you said. ')
# if q==1:
#     continue()
# elif q==2:
#     exit()

# file = open('today.txt', 'r')
# contents = file.readlines()
# for line in contents:
#     print(line)
# print(contents)
# file.close()
#
# with open('today.txt', 'r') as file:
#     contents = file.readlines()
#     for line in contents:
#         print(line)

def read_file (file_path):
    with open (file_path, 'r') as file:
        contents = file.readlines()
        for line in contents:
            print(line)
    print(contents)

def write_file(file_path):
    with open(file_path, 'w') as file:
        times = int(input("What would like to write to this file?: "))
        ran = 0
        list_of_lines = []
        while ran < times:
            list_of_lines.append(input("What would like to write to this file?: "))
            ran +=1
        for line in list_of_lines:
            file.write(line + '\n')

write_file('today.txt')
read_file('today.txt')

import sys

phonebook = {
    'Watters':{'name': 'Kasey Watters', 'phone': 3333333333},
    'Magnuson':{'name': 'Tom Magnuson', 'phone': 4444444444},
    'Yeaney': {'name': 'Johnny Yeaney', 'phone': 5555555555},
}

def my_function():
    while True:
        print('              WELCOME TO THE PHONEBOOK LAB       ')
        user = input("""
        Enter 1 if you want to search directory,
        2 if you want to add an entry,
        3 if you want to change an entry,
        4 if you want to delete an entry or
        5 if you want to exit program.
        """)

        if user == '1':
            query = input("What is the last name of the person you are searching? ")
            print(phonebook[query.capitalize()]['name'])
            print(phonebook[query.capitalize()]['phone'])
            pass


        elif user == '2':
            query = input("Type the last name of the person ")
            query2 = input("Type the first name of the person  ")
            query3 = int(input("Type the phone number of the person "))
            fullname = ('{} {}'.format(query2.capitalize(),query.capitalize()))
            phonebook[query.capitalize()] = {'name': fullname, 'phone':query3}
            print(phonebook)
        elif user == '3':
            change = input("Type the last name of the entry you want to change ")
            # print(query)
            del phonebook[change.capitalize()]
            print(phonebook)
            query = input("Type the last name of the person ")
            query2 = input("Type the first name of the person  ")
            query3 = int(input("Type the phone number of the person "))
            fullname = ('{} {}'.format(query2.capitalize(),query.capitalize()))
            phonebook[query.capitalize()] = {'name': fullname, 'phone':query3}
            print(phonebook)
        elif user == '4':
            query = input("Type the last name of the entry you want to delete ")
            # print(query)
            del phonebook[query.capitalize()]
            print(phonebook)
        elif user == '5':
            sys.exit("Good Bye")
        else:
            pass


my_function()

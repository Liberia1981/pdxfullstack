phone_book = {}

def display():
    print("")
    print("Here are the entries in the phone book: ")
    for key in phone_book:
        print("")
        print(key)
        print("")

def search():
    running = True
    while running == True:
        search_name = input("Whose number do you want to find?: ")
        for i in phone_book.keys():
            if search_name == i:
                print("")
                print("{}'s phone number is: {}.".format(search_name, phone_book[search_name].get("phonenumber")))
            else:
                print("")
                print("I couldn't find anyone by that name. ")
        if input("Do you want to search again? (y/n?): ") == "n":
            running = False

def add_entry():
    running = True
    while running == True:
        add_name = input("Whose number do you want to add?: ")
        add_number = str(input("What is {}'s phone number to add to the phone book?: ".format(add_name)))
        phone_book[add_name] = {"phonenumber": add_number}
        # print(add_name)
        # print(add_number)
        # print(phone_book)
        if input("Do you want to add anyone else? (y/n?): ") == "n":
            running = False

def change_entry():
    running = True
    while running == True:
        display()
        # print("")
        # print("Here are the entries in the phone book: ")
        # for key in phone_book:
        #     print("")
        #     print(key)
        #     print("")
        change_name = input("Whose number do you want to update?: ")
        if change_name in phone_book:
            change_number = str(input("What is {}'s new phone number?: ".format(change_name)))
            phone_book.update({change_name: {"phonenumber":change_number}})
        #print(phone_book)
        else:
            print("")
            print("No one by that name in the phone book.  Go back to add new entries.")
            print("")
        if input("Do you want to update anyone else's number? (y/n?): ") != "y":
            running = False

def delete_entry():
    running = True
    while running == True:
        display()
        delete_name = input("Which name would you like to delete?")
        if delete_name not in phone_book:
            print("")
            print("No one by that name in the phone book.  Go back to delete entries.")
            print("")
        else:
            phone_book.pop(delete_name)
            print("")
            print("{}'s entry was deleted".format(delete_name))
            print("")
        if input("Do you want to update anyone else's number? (y/n?): ") != "y":
            running = False

selection = 0

while selection != 6:
    selection = int((input("Phonebook.  Press 1 to search, 2 to Add Entry, 3 to Change Entry, 4 to Delete Entry, 5 to display the book, and 6 to exit: ")))
    if selection == 1:
        search()
    elif selection == 2:
        add_entry()
    elif selection == 3:
        change_entry()
    elif selection == 4:
        delete_entry()
    elif selection == 5:
        display()
    elif selection == 6:
        quit()
    else:
        print("")
        print("Please make a valid selection. ")
        print("")

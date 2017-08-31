import random
while True:
    a = input("Enter yes/no to continue")
    if a=="yes":
        Born = input("Give me an antonym for 'Born' ")
        chalk = input("Give me an adjective ")
        laughs = input("Give me a verb ")
        elevators = input("A type of object that transports people ")
        ls = input('Type three jobs typically done by high school schoolers separated by commas ')
        words = ls.split(",")
        print(words)
        supermarket_bag_boy = random.choice(words)
        fish = input("Name an animal that is oily ")
        wars = input("A dangerous place(noun) ")
        emptiness = input("A synonym for emptiness ")
        print(Born, """like this
        Into this
        As the""", chalk, """faces smile
        As Mrs. Death,""", laughs,
        "As the", elevators, """break
        As political landscapes dissolve
        As the""", supermarket_bag_boy, """holds a college degree
        As the oily""", fish, """spit out their oily prey
        As the sun is masked
        We are""",)
        print(Born, """like this
        Into this
        Into these carefully mad""", wars)
        print("Into the sight of broken factory windows of", emptiness)

    elif a=="no":
        break
    else:
        print("Enter either yes/no")
#this is for while loop
#https://stackoverflow.com/questions/22362165/i-want-to-have-a-yes-no-loop-in-my-code-but-im-having-trouble-doing-it-python

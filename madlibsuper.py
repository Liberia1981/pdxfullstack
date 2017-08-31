import random
Born = input("Give me an antonym for 'Born' ")
chalk = input("Give me an adjective ")
laughs = input("Give me a verb ")
elevators = input("A type of object that transports people ")
ls = input('Type three jobs typically done by high school schoolers separated by commas ')
words = ls.split(",")
print(words)
supermarket_bag_boy = random.choice(words)
#https://stackoverflow.com/questions/4071396/split-by-comma-and-strip-whitespace-in-python
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

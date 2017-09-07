# # Practice: Road Trip
#
# In a faraway land, nearby cities are connected by roads.
# We've mapped what cities are directly connected by roads and stored them in a dict:
def display_message():
    print("===========================================")
    print("****            RoadTrip        ****")
    print("===========================================")
    print("****Going on a Motherfucking RoadTrip****")
    print("===========================================")
    print("****            RoadTrip        ****")
    print("===========================================")
display_message()



city_to_accessible_cities = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'}
}
city=['Boston','New York','Albany','Portland','Philadelphia',]
# y=input("Input city you would like to see the cities direclty connected by roads are: ")
# x=y.lower()
while True:
    y=input("Input city you would like to see the cities direclty connected by roads are: ")
    x=y.lower()
    if x=='boston':
        print(city_to_accessible_cities['Boston'])
        question1=input("Do you want to keep playing? y for yes and any character for no: ")
        if question1=='y':
            qustion1=display_message()
        else:
            break
    elif x=='new york':
        print(city_to_accessible_cities['New York'])
        question1=input("Do you want to keep playing? y for yes and any character for no: ")
        if question1=='y':
            qustion1=display_message()
        else:
            break
    elif x=='albany':
        print(city_to_accessible_cities['Albany'])
        question1=input("Do you want to keep playing? y for yes and any character for no: ")
        if question1=='y':
            qustion1=display_message()
        else:
            break
    elif x=='portland':
        print(city_to_accessible_cities['Portland'])
        question1=input("Do you want to keep playing? y for yes and any character for no: ")
        if question1=='y':
            qustion1=display_message()
        else:
            break
    elif x=='philadelphia':
        print(city_to_accessible_cities['Philadelphia'])
        question1=input("Do you want to keep playing? y for yes and any character for no: ")
        if question1=='y':
            qustion1=display_message()
        else:
            break
    else:
        question1=input("Do you want to keep playing? y for yes and any character for no: ")
        if question1=='y':
            qustion1=display_message()
        else:
            break
    # x=input("Incorrect input: Please input city you would like to see the cities direclty connected by roads are: ")
# if user types dictionary key print value

# print(city_to_accessible_cities)

# Traveling from one city to an adjacent one is called a **hop**.
#
# For this sort of problem, you'll want to iteratively visit cities you know you can access while updating:
# 1. Cities you can access.
# 1. Cities you've been to.
# 1. Cities you haven't been to.
#
# * Let the user enter a city.
# Print out all the cities connected to that city.
# * Let the user enter a city.
# Print out all cities that could be reached through two hops.
#
# ## Advanced
# * Let the user enter a city and a number of hops.
# Print out all cities that could be reached through that number of hops.
# * We've also mapped the travel time of each hop:
#
# python
# city_to_accessible_cities_with_travel_time = {
#   'Boston': {'New York': 4, 'Albany': 6, 'Portland': 3},
#   'New York': {'Boston': 4, 'Albany': 5, 'Philadelphia': 9},
#   'Albany': {'Boston': 6, 'New York': 5, 'Portland': 7},
#   'Portland': {'Boston': 3, 'Albany': 7},
#   'Philadelphia': {'New York': 9},
# }
#
# When the user enters a city and a number of hops, print out the shortest travel times to each city.
# Paths with fewer hops are not necessarily those with the shorter travel times.

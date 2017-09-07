# Lab: PyWeather

# Create a program that will propt a user for city name or zip code.
# Use that information to get the current weather. Display that information
# to the user in a clean way.
# https://stackoverflow.com/questions/20526905/calling-function-inside-if-statement

import requests
def display_message():
    print("=============================")
    print("****   PyWeather   ****")
    print("=============================")
    print("CITY OR ZIP CODE TEMPERATURE")
    print("=============================")
    print("1 FOR CITY OR 2 FOR ZIP CODE")
    print("=============================")
display_message()


user_question=int(input("INPUT: "))


def zipcoder(package3):
    package = {
      'APPID': "6e2e08a69687bf4c11d139767e4c7b91",
      'zip': 97203,
      'units': 'Imperial'
    }
    package['zip']=package3
    r = requests.post('http://api.openweathermap.org/data/2.5/weather', params=package)
    data = r.json()
    x=int(data['main']['temp'])
    print("The temp. for that zip is:",x,"Fahrenheit")


def cityname(city3):
    package = {
      'APPID': "6e2e08a69687bf4c11d139767e4c7b91",
      'name': 'London',
    }
    print(city3)
    package['name']='Carins'
    r = requests.post('http://api.openweathermap.org/data/2.5/weather', params=package)
    data = r.json()
    print(data)

if user_question == 2:
    package3 = int(input("Type a zip code: "))
    zipcoder(package3)
else:
    user_question == 1
    city3 = input("Type name of a city: ")
    cityname(city3)

while True:
     play_again = input("Do you want to play again (type yes or any character for no): ")
     if play_again == "yes":
        user_question=int(input("INPUT:  1 for City or 2 for Zip Code: "))
        if user_question == 2:
            package3 = int(input("Type a zip code: "))
            zipcoder(package3)
        else:
            user_question == 1
            city3 = input("Type name of a city: ")
            cityname(city3)
     else:
         break

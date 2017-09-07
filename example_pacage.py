import requests

# r = requests.get('http://api.icndb.com/jokes/random')
#
# data = r.json()
#
#
# print('Joke #{}'.format(data['value']['id']))
# print('{}'.format(data['value']['joke']))

package = {
  'APPID': "6e2e08a69687bf4c11d139767e4c7b91",
  'q': 'London',
  'units': 'Imperial'
}

r = requests.post('http://api.openweathermap.org/data/2.5/weather?', params=package)
data = r.json()
x=int(data['main']['temp'])
print("The temp. for that zip is:",x,"Fahrenheit")


# dictionary = { 1: 'one', 2:'two', 3:'three' }
# print(dictionary)
# dictionary['ONE'] = dictionary.pop(1)
# print(dictionary)

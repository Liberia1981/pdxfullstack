# import requests
#
# r = requests.get('http://api.icndb.com/jokes/random')
#
# data = r.json()
#
#
# print('Joke #{}'.format(data['value']['id']))
# print('{}'.format(data['value']['joke']))

dictionary = { 1: 'one', 2:'two', 3:'three' }
print(dictionary)
dictionary['ONE'] = dictionary.pop(1)
print(dictionary)

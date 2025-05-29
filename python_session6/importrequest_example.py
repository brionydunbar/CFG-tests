import requests
from pprint import pprint

# this endpoint tells the current location for international space station
endpoint = 'http://api.open-notify.org/iss-now.json'

response = requests.get(endpoint)

data = response.json()
print(data)


# this endpoint gives us HP students
endpoint = 'https://hp-api.onrender.com/api/characters/students'

response = requests.get(endpoint)

data = response.json()
pprint(data)

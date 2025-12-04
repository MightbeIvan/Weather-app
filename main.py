import requests
import json

# Read API key from file
# api_key = open('api_key.txt', 'r').read().strip()

# Ask user for location
location = input("What Location's weather would you like to see?: \n> ")

# Correct URL format
url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid=6b6fd6ef03e57c965e9ed142598b7a14'

# Make request
result = requests.get(url)

# Print JSON response
information=result.json()
print(json.dumps(information, indent=4))

#get Main Weather...
# print(information["weather"][0]["main"])

#Get Decription of main weather
# print(information["weather"][0]["description"])





print("In",location,"it is currently: ",information["weather"][0]["main"],"\n The dicription is")
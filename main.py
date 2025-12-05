import requests
import json
import time
import os
import math




#MAIN WEATHERS!

#Get the temmpreture.
# print(information["weather"][0]["temp"])

#get Main Weather...
# print(information["weather"][0]["main"])

#get the cloud percentage
#print(informmation)["clouds"][0]["all"]

#Get Decription of main weather
# print(information["weather"][0]["description"])

#Get what the weather feels like
#print(informmation)["main"][0]["feels_like"]

#Get the hummidity level
#print(informmation)["main"][0]["humiidity"]


#WIND SPEEDS!

#Get the wind speed
#print(informmation)["wind"][0]["speed"]


#Get the direction the wind is blowing from.
#note: 
# 0° — North
# 45° — Northeast
# 90° — East
# 135° — Southeast
# 180° — South
# 225° — Southwest
# 270° — West
# 315° — Northwest

#Get the gust of the wind
#print(informmation)["wind"][0]["gust"]

#LOCATION

#get the location (might have an error)
##print(informmation)["sys"][1]["country"]


#get the local time(your time)(using time module)
# print(time.localtime())




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




print("In",location,"it is currently: ",information["weather"][0]["main"],"\n The dicription of the weather is",information["weather"][0]["description"])
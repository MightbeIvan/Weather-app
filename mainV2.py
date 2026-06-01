import requests
import json
import time
import os
import math
import sys
os.system('cls||clear')
#Control the While Loop
play = True 

#Class
class WeatherApp:
    def __init__(self,location):
        self.location = location
        self.api_key = "API_KEY"
        self.url = f' https://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid=6b6fd6ef03e57c965e9ed142598b7a14'
        self.information = {}
        
    def getWeather(self):
        result = requests.get(self.url)
        self.information = result.json()
        
    def showCelsius(self):
        temp = self.information ["main"]["temp"]
        
        print(f"\n Tempreture is in {self.location}: {temp} C")
        
    def showHumidity(self):
        humidity = self.information ["main"]["humidity"]
        
        print(f"Humidity: {humidity}")
        
    def showWind(self):
        wind = self.information["wind"]["speed"]
        
        print(f"wind Speed: {wind} m/s")
        


#Functions

def runagain(): #Loops through the code.
    again=input("Would you like to do something else (yes/no)\n>").lower().strip().replace(" ","")
    if again == "yes" or again == "y":
        return True
    elif again == "no" or again == "n":
        return False

def intoFahrenheit(celsius): #changes celcius to fahrenheit 
     return (celsius * 9/5) + 32
 


def print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


#Asking for a Location
print("Enter Location:")
location = input(">")

app = WeatherApp(location)
app.getWeather()
app.showCelsius()
app.showHumidity()
app.showWind()

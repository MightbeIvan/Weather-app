import requests
import json
import time
import os
import math
import sys
from datetime import datetime

os.system('cls||clear')
# os.system('color 1f')

#Control the While Loop
running = True 

#Class
class WeatherApp:
    def __init__(self,location):
        self.location = location 
        self.api_key = "API_KEY"
        self.url = f' https://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid=6b6fd6ef03e57c965e9ed142598b7a14'
        # self.forecast_url = "https://api.openweathermap.org/data/4.0/onecall/timeline/1h?lat={lat}&lon={lon}&appid={location}}"
        self.information = {}
        
    def hourlyWeather(self):
        result = requests.get(self.forecast_url)
        self.information = result.json()

    def getWeather(self):
        result = requests.get(self.url)
        self.information = result.json()
        
        if result.status_code != 200:
            type("Location not found.")
            return False 
        return True
        
    def showCelsius(self):
        temp = self.information ["main"]["temp"]
        
        type(f"\n Tempreture is in {self.location}: {temp} C")
        
    def showHumidity(self):
        humidity = self.information ["main"]["humidity"]
        
        type(f"Humidity: {humidity}")
        
    def showWind(self):
        wind = self.information["wind"]["speed"]
        
        type(f"wind Speed: {wind} m/s")
        
    def showDescription(self):
        description = self.information["weather"][0]["description"]

        type(f"Conditions: {description.title()}")
        
    def showFeelsLike(self):
        feels_like = self.information["main"]["feels_like"]

        type(f"Feels Like: {feels_like}°C")
        


#Functions
def runagain(): 
    type("Would you like to do something else (yes/no)")
    again=input("> ").lower().strip().replace(" ","")
    
    if again == "yes" or again == "y":
        return True
    elif again == "no" or again == "n":
        return False

def intoFahrenheit(celsius): #changes celcius to fahrenheit 
        return (celsius * 9/5) + 32


def type(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loadingAnimation(): # loading effect
    loadingtime = 5
    for i in range(loadingtime):
        os.system('cls||clear')
        (type("Loading . . . "))
        os.system('cls||clear')
        time.sleep(0.2)

'''////////////////////////////////////////////////////////////////////////////////////////////////////////'''

#Main Algorithm
while running == True:

    print("\033[1m" + "Welcome to weather app v2" + "\033[0m")
    print()

    type("What would you like to do today:")
    print()

    type("(1) See the Weather.")
    print()

    type("(2) See the Humidity.")
    print()

    type("(3) See the Wind-Speeds.")
    print()

    type("(4) Weather Description.")
    print()

    type("(5) Show All.")
    print()

    type("(6) Exit Program.")
    print()                                                                         
    
    userdoing = input("> ").strip()
    
    # Handle direct exit first
    if userdoing == "6":

            type("Thank you for using weatherApp-V2. Goodbye!")
            break
        
    # Validation 
    if userdoing not in ["1", "2", "3", "4", "5"]:
        type("Invalid option. Please choose a number between 1 and 6.")
        print()
        os.system('cls||clear')
        continue
        
    # Get location for options 1-5
    os.system('cls||clear')
    type("\nEnter Location Name(City,Country):")
    
    city = input("> ").strip()
    app = WeatherApp(city)
    if not app.getWeather():
        print()
        running = runagain()
        os.system('cls||clear')
        continue


    
    # Process the user's choice
    if userdoing == "1":
        os.system('cls||clear')
        loadingAnimation()
        print()
        type("-" * 30)
        app.showCelsius()
        celsius_temp = app.information["main"]["temp"] 
        fahrenheit_temp = intoFahrenheit(celsius_temp)
        type(f" Temperature in Fahrenheit: {fahrenheit_temp:}°F")
        type("-" * 30)
        
    elif userdoing == "2":
        os.system('cls||clear')
        loadingAnimation()
        print()
        type("-" * 30)
        app.showHumidity()
        type("-" * 30)
        
    elif userdoing == "3":
        os.system('cls||clear')
        loadingAnimation()
        print()
        type("-" * 30)
        app.showWind()
        type("-" * 30)
        
    elif userdoing == "4":
        os.system('cls||clear')
        loadingAnimation()
        print()
        type("-" * 30)
        app.showDescription()
        app.showFeelsLike()
        type("- " * 30)
        
    elif userdoing == "5":
        os.system('cls||clear')
        loadingAnimation()
        print()
        type("-" * 30)
        app.showCelsius()
        celsius_temp = app.information["main"]["temp"]
        type(f" Temperature in Fahrenheit: {intoFahrenheit(celsius_temp):.1f}°F")
        app.showFeelsLike()
        app.showDescription()
        app.showHumidity()
        app.showWind()
        type("-" * 30)

        
    
    # Check if user wants to look up another city or quit
    running = runagain()
    os.system('cls||clear')

type("Thank you for using weatherApp-V2. Goodbye!")

import requests
import json
import time
import os
import math
import sys
from datetime import datetime

os.system('cls||clear')
#Control the While Loop
running = True 

#Class
class WeatherApp:
    def __init__(self,location):
        self.location = location
        self.api_key = "API_KEY"
        self.url = f' https://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid=6b6fd6ef03e57c965e9ed142598b7a14'
        self.forecast_url = "https://api.openweathermap.org/data/2.5/forecast"
        self.information = {}
        
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

def runagain(): #Loops through the code.
    type("Would you like to do something else (yes/no)\n>")
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


###########?//////////////////////////////////////////?#######




#Main Algorithm
while running == True:
    
    type("Welcome to weatherApp-V2.")
    type("What would you like to do today:")
    
    type(""" (1) See the Weather.
          
 (2) See the Humidity.
 
 (3) See the Wind-Speeds.
 
 (4) Weather Description.
 
 (5) Show All.
 
 (6) Exit Program.""")
    
    userdoing = input("> ").strip()
    
    # Handle direct exit first
    if userdoing == "6":
        type("Thank you for using weatherApp-V2. Goodbye!")
        break
        
    # Validation for choices 1-5
    if userdoing not in ["1", "2", "3", "4", "5"]:
        type("Invalid option. Please choose a number between 1 and 6.")
        print()
        continue
        
    # Get location for options 1-5
    type("\nEnter city name:")
    
    city = input("> ").strip()
    app = WeatherApp(city)
    if not app.getWeather():
        print()
        running = runagain()
        os.system('cls||clear')
        continue

    type("-" * 30)
    
    # Process the user's choice
    if userdoing == "1":
        app.showCelsius()
        # Optional: Display Fahrenheit using your intoFahrenheit function
        celsius_temp = app.information["main"]["temp"]
        fahrenheit_temp = intoFahrenheit(celsius_temp)
        type(f" Temperature in Fahrenheit: {fahrenheit_temp:.1f}°F")
        
    elif userdoing == "2":
        app.showHumidity()
        
    elif userdoing == "3":
        app.showWind()
        
    elif userdoing == "4":
        app.showDescription()
        app.showFeelsLike()
        
    elif userdoing == "5":
        # Show everything combined neatly
        app.showCelsius()
        celsius_temp = app.information["main"]["temp"]
        type(f" Temperature in Fahrenheit: {intoFahrenheit(celsius_temp):.1f}°F")
        app.showFeelsLike()
        app.showDescription()
        app.showHumidity()
        app.showWind()
        
        
    print("-" * 30)
    
    # Check if user wants to look up another city or quit
    running = runagain()
    os.system('cls||clear')

type("Thank you for using weatherApp-V2. Goodbye!")

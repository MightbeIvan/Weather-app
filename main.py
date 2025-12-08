import requests
import json
import time
import os
import math
play = True



#Functions 

def runagain(): #Loops through the code.
    again=input("Would you like to do something else (yes/no)\n>").lower().strip().replace(" ","")
    if again == "yes" or again == "y":
        return True
    elif again == "no" or again == "n":
        return False

def intoFahrenheit(celsius): #changes celcius to fahrenheit 
     return (celsius * 9/5) + 32
    








print("Welcome to the weather program,This program is designed to tell you the weather of a specific place.\n")
 #Correct URL format


#

#

while play == True:
    #inputs
    Location = input("What Location's weather would you like to see?: \n> ").strip().capitalize().replace(" ","")
    url = f'https://api.openweathermap.org/data/2.5/weather?q={Location}&units=metric&appid=6b6fd6ef03e57c965e9ed142598b7a14'
    result = requests.get(url)
    information=result.json()
    print(json.dumps(information, indent=4))
    print()
    print("You picked",Location,"\n")


    print("we offfer a lot of different services for the weather such as\n")


    print(" •(1)See the weather tempreture in celsius")#and what it feels like

    print(" •(2)see the weather tempreture in Fahrenheit")#and what it feels like

    print(" •(3)see the description of the main weather")

    print(" •(4)see the main weather")

    print(" •(5)see the cloud percentage")

    print(" •(6)see the humidity level")

    print(" •(7)see the wind speeds")

    print(" •(8)see which dirrection the winds are blowing")

    print(" •(9)see the gust of wind")

    print(" •(all)See all the options above at the same time")

    print(" •(exit)Exit out of the program")
    print()

    options=input("what type of weather would you like to see?(Enter the number, 'all' or 'exit') \n >").lower().strip().replace(" ","")

    if options == "1":
       print("The temperature in", Location,"in Celsius is currently",information["main"]["temp"],"degrees.")
       play = runagain()
        
        
    elif options == "2":
        print("The tempreture in",Location,"is currently",intoFahrenheit(information["main"]["temp"]))
        play = runagain()
        
    elif options == "3":
        print("The Description of the main weather in",Location,"is ")
        play = runagain()
        
    elif options =="4":
        print("The Main")
        play = runagain()
        
    elif options =="5":
        print("The percentage of clouds in",Location,"is ")
        play = runagain()
        
    elif options =="6":
        print("The Humidity level in ",Location,"is")
        play = runagain()
        
    elif options == "7":
        print("The wind speeds in",Location,"is ")
        play = runagain()
        
    elif options=="8":
        print("The Wind is blowing ...")
        play = runagain()
        
    elif options == "9":
        print("The gust in",Location,"is")
        play = runagain()
        
    elif options == "all":
        print("test")
        play = runagain()
        
    elif options == "end":
        print("Ts should end the loop")
    else:
        print("This response is invalid,Start over.")

# weather app!!

Finds the weather of any location with the help of apis

# Description
This program gets the weather of any location and displays it on the command!


## Dependancies
* if statements 
* python
* OS module
* while loop
* - continue
* - break
* dictionary
* list 

### Executing the Program
r IDE, make sure you are in the project folder in the terminal and type: 
```sh
python .py
``` 

### Authors

[MightbeIvan | Github](https://github.com/MightbeIvan)



### Other important information about the program

*Get the temmpreture.
-print(information["weather"][0]["temp"])

*get Main Weather...
-print(information["weather"][0]["main"])

*get the cloud percentage
-print(informmation)["clouds"][0]["all"]

*Get Decription of main weather
-print(information["weather"][0]["description"])

*Get what the weather feels like
-print(informmation)["main"][0]["feels_like"]

*Get the hummidity level
-print(informmation)["main"][0]["humiidity"]

*WIND SPEEDS!

*Get the wind speed
-print(informmation)["wind"][0]["speed"]


*Get the direction the wind is blowing from.

-0° — North
-45° — Northeast
-90° — East
-135° — Southeast
-180° — South
-225° — Southwest
-270° — West
-315° — Northwest

*Get the gust of the wind
-print(informmation)["wind"][0]["gust"]

*LOCATION

*get the location (might have an error)
-print(informmation)["sys"][1]["country"]


*get the local time(your time)(using time module)
-print(time.localtime())


*Read API key from file
-api_key = open('api_key.txt', 'r').read().strip()

*°C
*°F
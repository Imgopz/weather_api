#!/usr/bin/env python3

# importing libraries
import requests

# variables
api_url = 'https://api.openweathermap.org/data/2.5/weather?q=Philadelphia,Pennsylvania,UnitedStates&appid=1c2ec9787e31a8befd61e8caff833927'

# api request and loading JSON data
json_data = requests.get(api_url).json() 

# fetching and calculating temperature value and fetching humidity value from JSON result
tempC = int(json_data['main']['temp'] - 273.15)
tempF = int(int(json_data['main']['temp'] - 273.15) * 9/5 + 32)
humidity = int(json_data['main']['humidity'])

# priting the result
print('\n*********Philadelphia, Pennsylvania, United States*********')
print('\nTemperature: ' + str(tempC) + ' \N{DEGREE SIGN}C | ' + str(tempF) + ' \N{DEGREE SIGN}F')
print('Humidity: ' + str(humidity) + ' %')
print('\n*************************END*******************************')


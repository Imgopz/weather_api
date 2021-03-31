#!/usr/bin/env python3
# importing libraries
import pyowm

# loading api key
owm = pyowm.OWM('1c2ec9787e31a8befd61e8caff833927')

# observing and getting weather details for a specified location
observation = owm.weather_at_place('Philadelphia, Pennsylvania, United States')
w = observation.get_weather()

# fetching values from the weather details
tempC = w.get_temperature('celsius')
tempF = w.get_temperature('fahrenheit')
status = w.get_detailed_status()
humidity = w.get_humidity()

# displaying values 
print('\n*********Philadelphia, Pennsylvania, United States*********')
print('\nTemperature: ' + str(int(tempC['temp'])) + ' \N{DEGREE SIGN}C | ' + str(int(tempF['temp'])) + ' \N{DEGREE SIGN}F')
print('Humidity: ' + str(humidity) + ' %')
print('\n*************************END*******************************')
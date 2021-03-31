#!/usr/bin/env python3

import pyowm

owm = pyowm.OWM('SECRET_API_KEY')
observation = owm.weather_at_place('Philadelphia, Pennsylvania, United States')
w = observation.get_weather()
tempC = w.get_temperature('celsius')
tempF = w.get_temperature('fahrenheit')
status = w.get_detailed_status()
humidity = w.get_humidity()

print('*********Philadlephia, Pennsylvania, United States*********')
print('Temperature: ' + str(int(tempC['temp'])) + ' \N{DEGREE SIGN}C | ' + str(int(tempF['temp'])) + ' \N{DEGREE SIGN}F')
print('Humidity: ' + str(humidity) + ' %')
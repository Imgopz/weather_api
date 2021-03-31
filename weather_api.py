import requests

api_url = 'https://api.openweathermap.org/data/2.5/weather?q=Philadelphia,Pennsylvania,UnitedStates&appid=1c2ec9787e31a8befd61e8caff833927'
json_data = requests.get(api_url).json() 
tempC = int(json_data['main']['temp'] - 273.15)
tempF = int(int(json_data['main']['temp'] - 273.15) * 9/5 + 32)
humidity = int(json_data['main']['humidity'])

print('\n*********Philadelphia, Pennsylvania, United States*********')
print('\nTemperature: ' + str(tempC) + ' \N{DEGREE SIGN}C | ' + str(tempF) + ' \N{DEGREE SIGN}F')
print('Humidity: ' + str(humidity) + ' %')
print('\n*************************END*******************************')


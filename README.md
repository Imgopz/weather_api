# weather_api
### Displaying live temperature and humidity at Philadelphia, Pennsylvania, United States.


## Using direct api url request
### File name: weather_api.py

Result:  
![](result_api.gif)

api.openweathermap.org/data/2.5/weather?q={city name},{state code},{country code}&appid={API key}

script executed: python3 weather_api.py


## Using PyOWM Library
### File name: weather.py

Result:  
![](result.gif)

Please install python3, pip3 and install pyowm 

PyOWM is a client Python wrapper library for OpenWeatherMap (OWM) web APIs. It allows quick and easy consumption of OWM data from Python applications via a simple object model and in a human-friendly fashion.

script executed: python3 weather.py

### Example output:
Philadelphia, Pennsylvania, United States   

Temperature: 15 °C | 60 °F    
Humidity: 94 %    


import requests

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid='

city_name = 'New Delhi'

response = requests.get(url.format(city_name)).json()



weather_of_city = {
        'city' : city_name,
        'temperature' : response['main']['temp'],
        'description' : response['weather'][0]['description'],
        'icon' : response['weather'][0]['icon'],
    }

print (weather_of_city)

degree_celsius = response['main']['temp'] - 273.15

print("Temp in degreee celsius:{:10.2f}".format(degree_celsius))
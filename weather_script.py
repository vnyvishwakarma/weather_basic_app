import requests

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid='

city_name = 'Lucknow'

res = requests.get(url.format(city_name)).json()
print(res)
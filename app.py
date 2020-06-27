# This application is using color from https://colorhunt.co/

import requests
from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid='
    city_name = 'Lucknow'
    response = requests.get(url.format(city_name)).json()

    temperature_in_degree = "{:10.2f}".format(((response['main']['temp']) - 273.15))

    weather_of_city = {
        'city' : city_name,
        'temperature' : temperature_in_degree,
        'description' : response['weather'][0]['description'],
        'icon' : response['weather'][0]['icon'],
    }

    print(weather_of_city)

    return render_template('index.html', weather = weather_of_city)

app.run()
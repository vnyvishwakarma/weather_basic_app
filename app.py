# This application is using color from https://colorhunt.co/

import requests
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' :
        city_name = request.form['city']

        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=8f5ca370c7041d066e0026e9af47526f'
        isError = 0

        try:
            response = requests.get(url.format(city_name)).json()
            temperature_in_degree = "{:10.2f}".format(((response['main']['temp']) - 273.15))
        except:
            print("An exception occurred")
            isError = 1
            return render_template('index.html', isError = isError, city= city_name)
        else:
            weather_of_city = {
                'city' : city_name,
                'temperature' : temperature_in_degree,
                'description' : response['weather'][0]['description'],
                'icon' : response['weather'][0]['icon'],
            }
            print(weather_of_city) 
            return render_template('index.html', weather = weather_of_city)

    else:

        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=8f5ca370c7041d066e0026e9af47526f'
        city_name = 'Lucknow'
        response = requests.get(url.format(city_name)).json()
        temperature_in_degree = "{:10.2f}".format(((response['main']['temp']) - 273.15))
        weather_of_city = {
            'city' : city_name,
            'temperature' : temperature_in_degree,
            'description' : response['weather'][0]['description'],
            'icon' : response['weather'][0]['icon'],
        }



        return render_template('index.html', weather = weather_of_city)
        


if __name__ == '__main__':
    app.run(debug=True)
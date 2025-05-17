from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = 'ffdda9979aaac8f4e49433d807e72281'  
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # For temperature in Celsius
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    print(f"Response: {data}")  # This will print the full response from OpenWeatherMap API
    
    if data['cod'] == 200:
        return data
    else:
        print(f"Error Code: {data['cod']}, Error Message: {data.get('message', 'No error message provided')}")
        return None

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', weather_data=None, error=None)

@app.route('/weather', methods=['GET'])
def weather():
    city = request.args.get('city')
    if city:
        weather_data = get_weather(city)
        if weather_data:
            return render_template('index.html', weather_data=weather_data, error=None)
        else:
            return render_template('index.html', weather_data=None, error="City not found or invalid. Please try again.")
    return render_template('index.html', weather_data=None, error="Please enter a city name.")

if __name__ == '__main__':
    app.run(debug=True)

import requests

API_KEY = 'your_openweathermap_api_key'  #  OpenWeatherMap API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # For temperature in Celsius
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    print(data)  # This will print the full response from OpenWeatherMap API
    
    if data['cod'] == 200:
        return data
    else:
        return None

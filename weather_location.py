import requests
from config import OPENWEATHER_URL, OPENWEATHER_TOKEN, GEOCODE_URL


# Получение координат по названию города
def get_location(city):
    geocode_params = {
        'q': city,
        'appid': OPENWEATHER_TOKEN,
        'limit': 1}

    response = requests.get(GEOCODE_URL, params=geocode_params)
    if response.status_code == 200 and response.json():
        return response.json()[0]['lat'], response.json()[0]['lon']
    return None


# Получение погоды по координатам
def get_weather(lat, lon):
    weather_params = {
        'lat': lat,
        'lon': lon,
        'appid': OPENWEATHER_TOKEN,
        'units': 'metric',  # температура в Цельсия
        'lang': 'ru'
    }
    response = requests.get(OPENWEATHER_URL, params=weather_params)
    if response.status_code == 200:
        return response.json()
    return None

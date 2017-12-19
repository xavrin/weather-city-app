from django.conf import settings
import requests

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&mode=html&APPID={settings.WEATHER_API_KEY}"
    res = requests.get(url)
    return res.content.decode('utf-8')

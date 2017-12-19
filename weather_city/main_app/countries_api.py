import requests
import json

base_url = "https://restcountries.eu/rest/v2"

def is_country_valid(country):
    url = f"{base_url}/name/{country}"
    res = requests.get(url)
    return res.status_code == 200

def get_capital(country):
    url = f"{base_url}/name/{country}"
    res = requests.get(url)
    data = json.loads(res.content)
    return data[0]["capital"]

import requests
api_key = '03bee4381ba34a6d8bd9c46be6597952'
city_name = 'London,UK'
params = {
        'lat': 47.03439729377494,
        'long': 28.842525531827274,
        'appid': api_key
        }
url = 'https://api.openweathermap.org/data/2.5/onecall'

response = requests.get(url=url, params=params)
response = response.json()
print(f"response: {response}")

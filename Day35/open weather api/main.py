import requests

OWM_Endpoint = 'http://api.openweathermap.org/data/2.5/onecall'
api_key = 'sdrfhgsdhfdshsdfhdshf'

weather_params = {
    'lat': 46.220196,
    'lon': -64.534683,
    'appid': api_key,


}

res = requests.get(OWM_Endpoint, params=weather_params)
print(res.json())
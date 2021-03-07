import requests

OWM_Endpoint = 'http://api.openweathermap.org/data/2.5/onecall'
api_key = 'eca730a1df1ecf4d3f885750343bb8b0'

weather_params = {
    'lat': 46.220196,
    'lon': -64.534683,
    'appid': api_key,
    'exclude': 

}

res = requests.get(OWM_Endpoint, params=weather_params)
print(res.json())
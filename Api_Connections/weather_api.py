import requests
import json
from Secrets.api_keys import WEATHER_API_KEY

# save zip and lat/lon to json file if zip does not change then just pull the lat and lon and skip location

def get_location(zip_code):
    url = f"https://api.openweathermap.org/geo/1.0/zip?zip={zip_code},US&appid={WEATHER_API_KEY}" 

    with requests.get(url) as response:
        print(response.status_code)
        if response.status_code == 200:
            data = response.json()
            lat = data['lat']
            lon = data['lon']
            location_JSON = {
                    'zip_code': zip_code,
                    'lat': lat,
                    'lon': lon
            }

            print('grabbed location')
            return location_JSON
        if response.status_code == 404:
            print('invalid zipcode')
            return 'invalid_zipcode'
    
def get_weather(zip_code, location_change, weather_data):
    # if location changed call the get_location function
    if location_change:
        weather_location = get_location(zip_code) 
        # check if valid location
        if weather_location == 'invalid_zipcode':
            return 'invalid_zipcode'
        else:
            lat = weather_location['lat']
            lon = weather_location['lon']
    else:
         lat = weather_data['lat']
         lon = weather_data['lon']

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}"

    with requests.get(url) as response:
        data = response.json()

        temp = data['main']['temp']
        weather_code =  data['weather'][0]['id']

        temp =  (temp * (9/5)) - 459.67
        weather_JSON = {
             'lat': lat,
             'lon': lon,
            'temp': temp,
            'weather_code': weather_code
        }
        print('grabbed weather')
        return weather_JSON
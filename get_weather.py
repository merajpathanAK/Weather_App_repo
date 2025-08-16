import requests



api_key = '34161ec40034e9cf9d40de37dc82f25d'

# A function that uses the requests libarary to make a GET 
# request to the OpenWeatherMap API for a certain location


def get_weather(location):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}'
    response = requests.get(url)
    weather_data = response.json()
    return weather_data
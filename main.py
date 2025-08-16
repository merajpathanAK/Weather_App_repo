from  get_weather import get_weather

# Ask user for their desired location to look up the weather for
location = input("Enter a location to get the weather: ") 

# Use the function in get_weather.py to get the weather for that location
weather_data = get_weather(location)
print(weather_data)

def convert_kelvin_to_celsius(kelvin_temp):
    """Convert Kelvin temperature to celsius."""
    celsius_temp = kelvin_temp - 273.15
    return celsius_temp

# Print the high and low temperature in celsius for the location
high_temp = convert_kelvin_to_celsius(weather_data['main']['temp_max'])
low_temp = convert_kelvin_to_celsius(weather_data['main']['temp_min'])
print(f"High: {high_temp:.2f}°C, Low: {low_temp:.2f}°C")
# Print the weather description for the location
weather_description = weather_data['weather'][0]['description'] 
print(f"Weather: {weather_description.capitalize()}")
# Print the humidity for the location
humidity = weather_data['main']['humidity']
print(f"Humidity: {humidity}%")
# Print the wind speed for the location
wind_speed = weather_data['wind']['speed']
print(f"Wind Speed: {wind_speed} m/s")
# Print the location name
location_name = weather_data['name']
print(f"Location: {location_name}")
# Print the country code
country_code = weather_data['sys']['country']
print(f"Country: {country_code}")
# Print the full weather data
print("Full Weather Data:")
print(weather_data)
# Print the current temperature in celsius
current_temp = convert_kelvin_to_celsius(weather_data['main']['temp'])
print(f"Current Temperature: {current_temp:.2f}°C")




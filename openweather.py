import requests
from datetime import datetime


api_key = 'your api key'

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def get_current_weather(location):
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'

    # Construct the complete URL with the location and API key
    complete_url = f"{base_url}q={location}&appid={api_key}"

    # Send a GET request to the OpenWeatherMap API
    response = requests.get(complete_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()

        # Extract and display real-time weather data
        temperature_kelvin = data['main']['temp']
        description = data['weather'][0]['description']  # Extract weather description from the API response

        # Convert temperature to Celsius and Fahrenheit
        temperature_celsius = kelvin_to_celsius(temperature_kelvin)
        temperature_fahrenheit = kelvin_to_fahrenheit(temperature_kelvin)

        # Get the current time and format it as AM/PM
        current_time = datetime.now().strftime("%I:%M %p")

        print(f"Current Weather in {location} at {current_time}:")
        print(f"Temperature: {temperature_celsius:.2f} °C")
        print(f"Temperature: {temperature_fahrenheit:.2f} °F")
        print(f"Description: {description}")
    else:
        print("Error: Unable to fetch current weather data")

if __name__ == '__main__':
    location = input("Enter a location (e.g., Punjab): ")
    get_current_weather(location)

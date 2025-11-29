import requests

def get_weather(city):
    try:
        GEOCODING_URL = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
        geo_response = requests.get(GEOCODING_URL)
        geo_data = geo_response.json()

        if not geo_data.get('results'):
            return f"Could not find the city: {city}"

        location_data = geo_data['results'][0]
        latitude = location_data['latitude']
        longitude = location_data['longitude']
        location_name = location_data['name']

        WEATHER_URL = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
        weather_response = requests.get(WEATHER_URL)
        weather_data = weather_response.json()
        
        temperature = weather_data['current_weather']['temperature']

        return f"Location: {location_name}, Temperature: {temperature}°C"

    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"
    except KeyError:
        return f"Could not parse weather data for {city}. Please try again."

city = input("Enter the name of the city: ")
print(get_weather(city))
import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Celsius
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        city = data['name']
        country = data['sys']['country']
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        print(f"\nWeather in {city}, {country}:")
        print(f"🌡 Temperature: {temperature}°C")
        print(f"🌤 Description: {description.capitalize()}")
        print(f"💧 Humidity: {humidity}%")
        print(f"🌬 Wind Speed: {wind_speed} m/s")
    else:
        print("❌ City not found or error fetching data.")

if __name__ == "__main__":
    print("🌍 Welcome to the Weather App!")
    city = input("Enter a city name: ").strip()
    api_key = "909837695b3d0228a0cc8541bbce21d0"
    get_weather(city, api_key)

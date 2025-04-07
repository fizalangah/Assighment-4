import streamlit as st
import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "City": data["name"],
            "Country": data["sys"]["country"],
            "Temperature (°C)": data["main"]["temp"],
            "Description": data["weather"][0]["description"].title(),
            "Humidity (%)": data["main"]["humidity"],
            "Wind Speed (m/s)": data["wind"]["speed"]
        }
    else:
        return None

# Streamlit UI
st.set_page_config(page_title="Weather App", layout="centered")
st.title("🌤 Weather Forecast App")
st.write("Enter your city below to get current weather information.")

city = st.text_input("City Name")
api_key = "909837695b3d0228a0cc8541bbce21d0"
#  = st.text_input("Enter your OpenWeatherMap API Key", type="password")

if st.button("Get Weather"):
    if city and api_key:
        weather = get_weather(city, api_key)
        if weather:
            st.success(f"Weather in {weather['City']}, {weather['Country']}")
            st.metric("🌡 Temperature", f"{weather['Temperature (°C)']} °C")
            st.metric("💧 Humidity", f"{weather['Humidity (%)']} %")
            st.metric("🌬 Wind Speed", f"{weather['Wind Speed (m/s)']} m/s")
            st.info(weather["Description"])
        else:
            st.error("City not found or invalid API key.")
    else:
        st.warning("Please enter both city and API key.")

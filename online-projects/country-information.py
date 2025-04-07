import streamlit as st
import requests

# Function to get country info
def get_country_info(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()[0]  # take the first result
        return {
            "Name": data["name"]["common"],
            "Capital": data.get("capital", ["N/A"])[0],
            "Region": data.get("region", "N/A"),
            "Population": f'{data.get("population", 0):,}',
            "Flag": data["flags"]["png"],
            "Timezone": ", ".join(data.get("timezones", [])),
            "Currency": list(data["currencies"].keys())[0] if "currencies" in data else "N/A",
            "Language": ", ".join(data["languages"].values()) if "languages" in data else "N/A"
        }
    else:
        return None

# Streamlit UI
st.set_page_config(page_title="Country Info Cards", layout="centered")
st.title("🌍 Country Information Cards")
st.write("Enter a country name to see its detailed information in a card format.")

# Input
country = st.text_input("🔍 Country Name")

# Button
if st.button("Show Info"):
    if country:
        info = get_country_info(country)
        if info:
            st.image(info["Flag"], width=200)
            st.markdown(f"""
            ### 🗺 {info['Name']}
            - **Capital:** {info['Capital']}
            - **Region:** {info['Region']}
            - **Population:** {info['Population']}
            - **Timezone(s):** {info['Timezone']}
            - **Currency:** {info['Currency']}
            - **Languages:** {info['Language']}
            """)
        else:
            st.error("❌ Country not found. Please check the spelling.")
    else:
        st.warning("Please enter a country name.")

import streamlit as st

def calculate_bmi(weight, height):
    bmi = weight / ((height / 100) ** 2)
    return round(bmi, 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight 🥗"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight ✅"
    elif 25 <= bmi < 29.9:
        return "Overweight ⚠️"
    else:
        return "Obese ❌"

# Streamlit UI
st.title("💪 BMI Calculator")

weight = st.number_input("Enter your weight (kg)", min_value=1.0, format="%.1f")
height = st.number_input("Enter your height (cm)", min_value=1.0, format="%.1f")

if st.button("Calculate BMI"):
    if weight and height:
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)
        st.success(f"Your BMI is: **{bmi}**")
        st.info(f"Category: **{category}**")
    else:
        st.error("Please enter valid weight and height!")

# Run the app using: streamlit run filename.py

import streamlit as st

st.title("BMI Calculator")

# Input fields
height = st.number_input("Enter your height (in cm):", min_value=50.0, max_value=300.0, step=1.0)
weight = st.number_input("Enter your weight (in kg):", min_value=10.0, max_value=300.0, step=1.0)

if st.button("Calculate BMI"):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    st.success(f"Your BMI is: {bmi:.2f}")

    # Optional: Add interpretation
    if bmi < 18.5:
        st.info("You are underweight.")
    elif 18.5 <= bmi < 25:
        st.success("You have a healthy weight.")
    elif 25 <= bmi < 30:
        st.warning("You are overweight.")
    else:
        st.error("You are obese.")

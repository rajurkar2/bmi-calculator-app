import streamlit as st

st.title("BMI Calculator")

# Input fields
height = st.number_input("Enter your height (in cm):", min_value=50.0, max_value=300.0, step=1.0)
weight = st.number_input("Enter your weight (in kg):", min_value=10.0, max_value=300.0, step=1.0)

if st.button("Calculate BMI"):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    st.success(f"Your BMI is: {bmi:.2f}")

    # Show BMI category and advice
    if bmi < 18.5:
        st.info("You are underweight.")
        st.caption("🍽️ Advice: Increase calorie intake with nutrient-rich foods like nuts, dairy, and whole grains.")
    elif 18.5 <= bmi < 25:
        st.success("You have a healthy weight.")
        st.caption("🥗 Advice: Maintain a balanced diet with regular physical activity.")
    elif 25 <= bmi < 30:
        st.warning("You are overweight.")
        st.caption("🥦 Advice: Reduce sugary and high-fat foods, and increase fiber intake.")
    else:
        st.error("You are obese.")
        st.caption("⚠️ Advice: Consult a dietitian and focus on a structured, calorie-controlled diet with exercise.")


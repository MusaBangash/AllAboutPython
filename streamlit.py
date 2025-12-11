
import streamlit as st


st.title("BMI Calculator")

weight = st.number_input("Weight (kg)")
height = st.number_input("Height (m)")

if st.button("Calculator"):
    bmi = weight/(height**2)
    st.write("Your BMI is:",bmi)
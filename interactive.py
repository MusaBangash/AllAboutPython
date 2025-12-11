import streamlit as st

st.set_page_config(page_title="Bank Form", layout="centered")

st.title("🏦 Welcome to Our Bank")
st.write("Please fill out your information below.")

with st.form("bank_form"):
    name = st.text_input("Full Name")
    contact = st.text_input("Contact Number")
    email = st.text_input("Email Address")

    submit = st.form_submit_button("Next")

if submit:
    if not name or not contact or not email:
        st.error("❗ Please fill all fields.")
    else:
        st.success("Information received!")
        st.write("### Customer Details:")
        st.write(f"**Name:** {name}")
        st.write(f"**Contact:** {contact}")
        st.write(f"**Email:** {email}")

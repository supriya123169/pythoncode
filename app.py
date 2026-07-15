import streamlit as st

# Title
st.title("Personal Information Form")

# Input fields
name = st.text_input("Enter Your Name")
age = st.number_input("Enter Your Age")

# Submit button
if st.button("Submit"):
    st.success("Information Submitted Successfully!")
    st.write("### Submitted Details")
    st.write(f"**Name:** {name}")
    st.write(f"**Age:** {age}")

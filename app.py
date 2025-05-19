import os
import google.generativeai as genai
import streamlit as st

# Configure API key
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Load model
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit UI
st.title(Math Tutor of Grade 8 International School of Cardoba Talagang")
user_input = st.text_input("Your question:", placeholder="e.g. The sum of three consecutive integers is 72. What are the integers?")

if user_input:
    with st.spinner("Thinking..."):
        try:
            response = model.generate_content(user_input)
            st.success("Expert says:")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"Error: {e}")

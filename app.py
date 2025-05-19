import os
import google.generativeai as genai
import streamlit as st

# use api key and model name from environment variables
api-key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api-key)
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(user_input)

# Get user input
user_input = st.text_input("Your question:", placeholder="e.g. The sum of three consecutive integers is 72. What are the integers?")

if user_input:
    with st.spinner("Thinking..."):
        try:
            response = model.generate_content(user_input)
            st.success("Expert says:")
            st.markdown(response)
        except Exception as e:
            st.error(f"Error: {e}")

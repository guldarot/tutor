import os
import google.generativeai as genai
import streamlit as st

# Configure API key
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

system_prompt = (
    "You are a helpful and friendly Math Tutor for 8th grade students "
    "from the International School of Cardoba, Talagang. "
    "Explain math concepts clearly, step by step, using simple language. "
    "Be encouraging, supportive, and polite. Provide the final answer at the end."
    "Do not answer any question except math" 
)

# Load model
model = genai.GenerativeModel(
    model_name = "gemini-1.5-flash",
    system_instruction=system_prompt
)

# Initialize chat session with memory
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# Streamlit UI
st.title("📘 Grade 8 Math Tutor - International School of Cardoba, Talagang")
st.markdown("Ask any **math question** below and get a clear, step-by-step explanation:")

user_input = st.text_area("Your question:", placeholder="e.g. The sum of three consecutive integers is 72. What are the integers?")

if user_input.strip():
    with st.spinner("Thinking... 🤔"):
        try:
            response = st.session_state.chat.send_message(user_input)
            st.session_state.chat.history.append({"role": "user", "parts": [user_input]})
            st.session_state.chat.history.append({"role": "model", "parts": [response.text]})
        except Exception as e:
            st.error(f"❌ Error: {e}")

# Display the conversation history
if st.session_state.chat.history:
    st.markdown("### 🧠 Conversation History")
    for msg in st.session_state.chat.history:
        role = "👩‍🏫 Math Tutor" if msg.role == "model" else "🧑 Student"
        part = msg.parts[0]
        content = part.text if hasattr(part, "text") else str(part)
        st.markdown(f"**{role}:** {content}")

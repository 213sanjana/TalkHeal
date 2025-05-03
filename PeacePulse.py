import streamlit as st
from PIL import Image
import base64
import time

# --- Set page configuration ---
st.set_page_config(page_title="PeacePulse", layout="wide")

# --- Set background from image file ---
def set_bg_from_local(img_path):
    with open(img_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    
st.markdown("""
    <style>
    .stApp {
        color: #111111; /* Dark text */
    }
    h1, h2, h3, h4, h5, h6 {
        color: #111111;
    }
    </style>
""", unsafe_allow_html=True)

# 🖼️ Replace this with the correct path to your image
set_bg_from_local("PeacePulseLogo.png")

# --- Title / Heading ---
st.markdown("<h1 style='text-align: center; color: black;'>Your Personal AI-based Mental Health Assistant :)</h1>", unsafe_allow_html=True)

# --- Issue Section ---
st.subheader("💬 What's your Issue ^-*?")
issue_input = st.text_input("Describe your issue here")

if st.button("🔍 Search for Help Resources"):
    if issue_input:
        search_term = issue_input.lower().replace(" ", "-")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"[🧭 HelpGuide](https://www.helpguide.org/?s={search_term})", unsafe_allow_html=True)
        with col2:
            st.markdown(f"[🧪 NIMH](https://www.nimh.nih.gov/search-nimh?q={search_term})", unsafe_allow_html=True)
        with col3:
            st.markdown(f"[🧠 Mind UK](https://www.mind.org.uk/search-results/?q={search_term})", unsafe_allow_html=True)

import google.generativeai as genai

# Configure Gemini
genai.configure(api_key="AIzaSyBeulOMD_D6_AUVdf1MKG6wnjxQ_gaSYsw")
model = genai.GenerativeModel('gemini-2.0-flash')

# Chatbot UI
st.subheader("🧠 Chat with PeacePulse AI Assistant")
chat_history = st.session_state.get("chat_history", [])
user_input = st.text_input("You:", key="chat_input")

if st.button("💬 Send"):
    if user_input:
        response = model.generate_content(user_input)
        chat_history.append(("You", user_input))
        chat_history.append(("PeacePulse AI", response.text))
        st.session_state.chat_history = chat_history

# Display chat history
for speaker, message in chat_history:
    st.markdown(f"**{speaker}:** {message}")

# --- Location-based Care Centres ---
st.subheader("📍 Where Do You Stay Friend?")
location_input = st.text_input("Enter your city or location")

if st.button("📌 Search Care Centres Near You"):
    if location_input:
        location_url = f"https://www.google.com/maps/search/Mental+Hospitals+and+trauma+care+centres+in+{location_input.replace(' ', '-')}/"
        st.markdown(f"[🗺️ View Nearby Centers on Google Maps]({location_url})", unsafe_allow_html=True)

# --- Professionals Help ---
st.subheader("👩‍⚕️ Some Specialists Who Can Help You :)")
if st.button("🔍 Find Mental Health Professionals"):
    st.markdown("[🌐 GoodTherapy Therapist Search](https://www.goodtherapy.org/therapists/search)", unsafe_allow_html=True)

# --- Developer Info & Date ---
st.markdown("---")
st.markdown("### 👨‍💻 Developed By:")
st.markdown("**Eccentric Explorer**  \n_“It's absolutely okay not to be okay :)”_", unsafe_allow_html=True)

st.markdown(f"📅 **Date:** {time.strftime('%d/%m/%y')}")

# --- Footer spacing ---
st.markdown("<br><br>", unsafe_allow_html=True)
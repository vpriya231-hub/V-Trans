import streamlit as st
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import os

# Page configuration
st.set_page_config(page_title="V-Trans", page_icon="🌐", layout="centered")

# Orange and White Professional Theme
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    h1 { color: #FF4B2B; text-align: center; font-family: 'Arial', sans-serif; }
    .stButton>button { 
        background-color: #FF4B2B; 
        color: white; 
        border-radius: 10px; 
        width: 100%;
        border: none;
        font-weight: bold;
    }
    .stTextArea textarea { border: 2px solid #FF4B2B; }
    p { text-align: center; color: #555; }
    </style>
    """, unsafe_allow_html=True)

st.title("V-Trans")
st.write("Speak or type — translate instantly into any language.")

# Initialize Translator
ts = Translator()
lang_map = {name.capitalize(): code for code, name in LANGUAGES.items()}

# Language selection with search feature
col1, col2 = st.columns(2)
with col1:
    from_lang = st.selectbox("From", ["Auto-detect"] + sorted(lang_map.keys()))
with col2:
    to_lang = st.selectbox("To", sorted(lang_map.keys()), index=sorted(lang_map.keys()).index("Malayalam"))

# Text input area
input_text = st.text_area("Input Text", placeholder="Enter text to translate...")

if st.button("Translate"):
    if input_text:
        try:
            dest_code = lang_map[to_lang]
            src_code = 'auto' if from_lang == "Auto-detect" else lang_map[from_lang]
            
            # Translation process
            output = ts.translate(input_text, src=src_code, dest=dest_code)
            
            st.markdown("### Translation:")
            st.success(output.text)
            
            # Voice Output (Text-to-Speech)
            tts = gTTS(text=output.text, lang=dest_code)
            tts.save("speech.mp3")
            st.audio("speech.mp3")
            
        except Exception as e:
            st.error("Connection error. Please check your internet and try again.")
    else:
        st.warning("Please enter some text first!")

st.markdown("---")
st.caption("Developed by Vishnu | V-Trans v1.0")


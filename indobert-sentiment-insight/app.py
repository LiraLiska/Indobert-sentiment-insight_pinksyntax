import streamlit as st
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import numpy as np
import torch

# Konfigurasi Halaman
st.set_page_config(page_title="IndoBERT Sentiment Insight", page_icon="🎀")

# CSS untuk tema Coquette Pink Pastel
st.markdown("""
    <style>
    /* Mengubah background utama */
    .stApp {
        background-color: #FFF0F5;
    }
    
    /* Judul dan Teks utama */
    h1, h2, h3, p, label {
        color: #D87093 !important;
        font-family: 'Georgia', serif;
    }
    
    /* Text Area Styling */
    .stTextArea textarea {
        background-color: #FFFFFF !important;
        color: #D87093 !important;
        border: 2px solid #FFC0CB !important;
        border-radius: 15px !important;
    }
    
    /* Tombol Styling */
    div.stButton > button {
        background-color: #FFC0CB !important;
        color: white !important;
        border: none !important;
        border-radius: 20px !important;
        font-weight: bold !important;
    }
    
    /* Hasil Styling */
    .stSubheader {
        background-color: #FFDEE9;
        padding: 10px;
        border-radius: 10px;
        border-left: 5px solid #D87093;
    }
    </style>
""", unsafe_allow_html=True)

# 1. Judul Aplikasi
st.title("🎀 IndoBERT Sentiment Insight")
st.write("Deep Learning-based sentiment classification for refined language understanding.")

# 2. Load Model & Tokenizer
@st.cache_resource
def load_model():
    model_path = "./model_akhir" 
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    return model, tokenizer

model, tokenizer = load_model()

# 3. Form Input User
user_input = st.text_area("Examine your text input here:", "")

if st.button("Execute Analysis"):
    if user_input:
        inputs = tokenizer(
            user_input,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=128
        )
        inputs = {k: v.to(model.device) for k, v in inputs.items()}

        with torch.no_grad():
            outputs = model(**inputs)
            prediction = np.argmax(outputs.logits.detach().cpu().numpy(), axis=-1)

        labels = ["Positive", "Negative", "Neutral"]
        result = labels[prediction[0]]

        st.subheader(f"Hasil: {result} 🌸")
    else:
        st.warning("Mohon tuliskan sesuatu ya! ✨")

if st.button("Execute Analysis"):
    if user_input:
        inputs = tokenizer(user_input, return_tensors="pt", truncation=True, padding=True, max_length=128)
        inputs = {k: v.to(model.device) for k, v in inputs.items()}
        
        with torch.no_grad():
            outputs = model(**inputs)
            prediction = np.argmax(outputs.logits.detach().cpu().numpy(), axis=-1)
        
        labels = ["Positive", "Negative", "Neutral"]
        result = labels[prediction[0]]
        
        st.subheader(f"Hasil: {result} 🌸")
    else:

        st.warning("Mohon tuliskan sesuatu ya! ✨")
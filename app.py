
import streamlit as st
import pandas as pd
import joblib


@st.cache_resource
def load_model():
    model = joblib.load("models/pollution_rf_model.pkl")
    le = joblib.load("models/label_encoder.pkl")
    return model, le

@st.cache_data
def load_data():
    return pd.read_csv("data/Final_Pollution_Hotspot_Dataset.csv")

model, le = load_model()
df = load_data()


st.set_page_config(page_title="AirGuard", page_icon="🌍", layout="wide")

st.title("🌍 AirGuard: India's Pollution Hotspot Intelligence Platform")
st.markdown("""
### 👋 Welcome to AirGuard  
This platform uses **machine learning, geospatial analytics, and AI-based insights** to:
- Detect and visualize **pollution hotspots**
- Predict **pollution severity for new cities**
- Compare **city-level pollution patterns**
- Recommend **targeted mitigation strategies**

📘 *All pollutant values represent averaged data over the past 5 years (2021–2026).*  
""")

st.info("👈 Use the sidebar to navigate through the analysis and prediction modules.")

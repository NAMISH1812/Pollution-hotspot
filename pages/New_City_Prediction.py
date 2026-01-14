

import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(page_title="New City Prediction", page_icon="🧮")

st.header("🧮 Predict Pollution Level for a New City")
st.caption("📘 *Enter pollutant levels to estimate pollution category using the trained Random Forest model.*")


model = joblib.load("models/pollution_rf_model.pkl")
le = joblib.load("models/label_encoder.pkl")


col1, col2, col3 = st.columns(3)
with col1:
    pm25 = st.number_input("PM2.5 (µg/m³)", min_value=0.0, step=0.1)
with col2:
    no2 = st.number_input("NO₂ (µg/m³)", min_value=0.0, step=0.1)
with col3:
    co = st.number_input("CO (mg/m³)", min_value=0.0, step=0.1)


if st.button("🔍 Predict Pollution Level"):
    if pm25 == 0 and no2 == 0 and co == 0:
        st.error("Please enter valid pollutant values.")
    else:
        
        X_new = np.array([[pm25, no2, co]])
        prediction = model.predict(X_new)[0]
        pollution_level = le.inverse_transform([prediction])[0]

        st.success(f"🏙️ Predicted Pollution Level: **{pollution_level}**")

        
        pollutants = {"PM2.5": pm25, "NO2": no2, "CO": co}
        dominant = max(pollutants, key=pollutants.get)

        st.warning(f"⚠️ Dominant Pollutant: **{dominant}**")

        
        if dominant == "PM2.5":
            st.info("💡 *Mitigation Tip:* Control construction dust, regulate vehicles, and increase green cover.")
        elif dominant == "NO2":
            st.info("💡 *Mitigation Tip:* Encourage electric vehicles and limit heavy-traffic emissions.")
        elif dominant == "CO":
            st.info("💡 *Mitigation Tip:* Improve air circulation, avoid idling vehicles, and promote CNG/LPG fuels.")
        
        
        st.subheader("📊 Pollutant Breakdown")
        pollutant_df = pd.DataFrame({
            "Pollutant": ["PM2.5", "NO2", "CO"],
            "Concentration": [pm25, no2, co]
        }).set_index("Pollutant")

        st.bar_chart(pollutant_df)


st.caption("📘 *Model trained on 5-year averaged data (2021–2026). Predictions reflect overall air quality trends.*")

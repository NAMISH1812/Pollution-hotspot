# -----------------------------------------------------------
# 📊 City-Wise Pollution Threats (Historical Overview)
# -----------------------------------------------------------

import streamlit as st
import pandas as pd

st.set_page_config(page_title="City-Wise Pollution Threats", page_icon="📊")

st.header("📊 City-Wise Pollution Threats")
st.caption("📘 *Displays average pollutant levels and pollution category for each city, based on 5-year data (2021–2026).*")

# Load dataset
df = pd.read_csv("data/Final_Pollution_Hotspot_Dataset.csv")

# City selector
city = st.selectbox("Select a City:", sorted(df['city'].unique()))

# Extract city data
city_data = df[df['city'] == city].iloc[0]

# Display key metrics
st.subheader(f"🏙️ {city}")
st.metric(label="Pollution Level", value=city_data['pollution_level'])
st.write(f"**PM2.5:** {city_data['pm25']:.1f} µg/m³")
st.write(f"**NO₂:** {city_data['no2']:.1f} µg/m³")
st.write(f"**CO:** {city_data['co']:.2f} mg/m³")

# Identify dominant pollutant
pollutants = {"PM2.5": city_data["pm25"], "NO2": city_data["no2"], "CO": city_data["co"]}
dominant = max(pollutants, key=pollutants.get)

st.warning(f"⚠️ Dominant Pollutant: **{dominant}**")

# Provide solution recommendation
if dominant == "PM2.5":
    st.info("💡 *Mitigation Tip:* Control construction dust, regulate vehicle emissions, and promote tree planting.")
elif dominant == "NO2":
    st.info("💡 *Mitigation Tip:* Reduce traffic congestion and switch to electric/public transport.")
elif dominant == "CO":
    st.info("💡 *Mitigation Tip:* Avoid idling vehicles, ensure proper ventilation, and promote cleaner fuels.")

# Optional visualization
st.subheader("📈 Pollutant Comparison")
pollutant_df = pd.DataFrame({
    "Pollutant": ["PM2.5", "NO2", "CO"],
    "Concentration": [city_data['pm25'], city_data['no2'], city_data['co']]
}).set_index("Pollutant")

st.bar_chart(pollutant_df)

# Add note
st.caption("📘 *Note: Pollutant values represent mean concentrations over the past 5 years (2021–2026).*")

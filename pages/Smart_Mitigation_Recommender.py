import streamlit as st
import pandas as pd

st.set_page_config(page_title="Smart Mitigation", page_icon="🌱")

st.header("🌱 Smart Mitigation Recommender")
st.caption("📘 *AI-based recommendations tailored for each city’s dominant pollutant.*")

df = pd.read_csv("data/Final_Pollution_Hotspot_Dataset.csv")

city = st.selectbox("Select a City", sorted(df['city'].unique()))
city_data = df[df['city'] == city].iloc[0]

dominant = max({
    'PM2.5': city_data['pm25'],
    'NO2': city_data['no2'],
    'CO': city_data['co']
}, key=lambda k: {'PM2.5': city_data['pm25'], 'NO2': city_data['no2'], 'CO': city_data['co']}[k])

st.write(f"🏙️ **City:** {city}")
st.write(f"**Dominant Pollutant:** {dominant}")
st.write(f"**Pollution Level:** {city_data['pollution_level']}")

if dominant == 'PM2.5':
    st.info("💡 *High PM2.5 levels detected.* Implement dust control, regulate construction, and encourage tree plantation.")
elif dominant == 'NO2':
    st.info("💡 *High NO₂ levels detected.* Encourage EVs, improve traffic management, and enhance fuel standards.")
elif dominant == 'CO':
    st.info("💡 *High CO levels detected.* Control vehicle idling and promote cleaner fuels.")
else:
    st.success("🌿 Air quality stable. Continue maintaining clean energy and transport initiatives.")

st.subheader("📊 Pollutant Breakdown")
st.bar_chart(pd.DataFrame({
    "Pollutant": ["PM2.5", "NO2", "CO"],
    "Concentration": [city_data['pm25'], city_data['no2'], city_data['co']]
}).set_index("Pollutant"))

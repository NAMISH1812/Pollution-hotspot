

import streamlit as st
import pandas as pd
import folium
from sklearn.cluster import KMeans
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster

st.set_page_config(page_title="Pollution Hotspot Map", page_icon="🌍")

st.header("🌍 Pollution Hotspot Map")
st.caption("📘 *Identifies pollution clusters using K-Means and visualizes city-level hotspots across India.*")


df = pd.read_csv("data/Final_Pollution_Hotspot_Dataset_with_Regional_Coordinates.csv")


if 'latitude' in df.columns and 'Latitude' not in df.columns:
    df.rename(columns={'latitude': 'Latitude', 'longitude': 'Longitude'}, inplace=True)


df = df.dropna(subset=['Latitude', 'Longitude'])
df = df[(df['Latitude'] > 5) & (df['Longitude'] > 60)]


kmeans = KMeans(n_clusters=4, random_state=42)
df['cluster'] = kmeans.fit_predict(df[['pm25', 'no2', 'co']])


cluster_colors = {
    0: 'green',     # Cleaner zones
    1: 'orange',    # Moderate pollution
    2: 'blue',      # High CO or NO₂ regions
    3: 'red'        # Severe PM2.5 hotspots
}


m = folium.Map(location=[22.97, 78.65], zoom_start=5, tiles="CartoDB positron")

marker_cluster = MarkerCluster().add_to(m)
selected_clusters = st.multiselect("Select clusters to display:", options=df['cluster'].unique(), default=df['cluster'].unique())
df = df[df['cluster'].isin(selected_clusters)]

for _, row in df.iterrows():
    radius = max(4, min(row['pm25'] / 8, 18))  
    color = cluster_colors.get(row['cluster'], 'gray')
    popup = (
        f"<b>{row['city']}</b><br>"
        f"Cluster: {row['cluster']}<br>"
        f"Pollution Level: {row['pollution_level']}<br>"
        f"PM2.5: {row['pm25']:.1f} µg/m³<br>"
        f"NO₂: {row['no2']:.1f} µg/m³<br>"
        f"CO: {row['co']:.2f} mg/m³"
    )
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=radius,
        color=color,
        fill=True,
        fill_opacity=0.6,
        popup=popup
    ).add_to(marker_cluster)


st_folium(m, width=750, height=500)


st.subheader("📈 Cluster Summary (Mean Pollutant Levels)")
cluster_summary = df.groupby('cluster')[['pm25', 'no2', 'co']].mean().round(1)
st.dataframe(cluster_summary)

st.caption("📘 *Marker colors represent clusters identified through unsupervised learning (K-Means) based on pollutant patterns.*")

import streamlit as st
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

st.set_page_config(page_title="Pollution Comparison", page_icon="🧩")

st.header("🧩 Pollution Comparison Across Cities")
st.caption("📘 *Compares cities based on pollution profiles using PCA (Principal Component Analysis).*")

df = pd.read_csv("data/Final_Pollution_Hotspot_Dataset.csv")

pca = PCA(n_components=2)
pca_result = pca.fit_transform(df[['pm25','no2','co']])
df['PC1'], df['PC2'] = pca_result[:, 0], pca_result[:, 1]

fig, ax = plt.subplots(figsize=(8,6))
sc = ax.scatter(df['PC1'], df['PC2'], c=df['pm25'], cmap='coolwarm', s=70)
for i, city in enumerate(df['city']):
    ax.annotate(city, (df['PC1'][i], df['PC2'][i]), fontsize=7, alpha=0.6)

ax.set_xlabel("Principal Component 1")
ax.set_ylabel("Principal Component 2")
ax.set_title("City Pollution Comparison (PCA Projection)")
plt.colorbar(sc, ax=ax, label="PM2.5")

st.pyplot(fig)

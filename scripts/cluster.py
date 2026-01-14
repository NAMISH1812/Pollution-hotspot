
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


df = pd.read_csv("data/City_Wise_Pollution_Index.csv")


def classify_pollution(index):
    if index <= 50:
        return 'Good'
    elif index <= 100:
        return 'Moderate'
    elif index <= 150:
        return 'Poor'
    elif index <= 250:
        return 'Very Poor'
    else:
        return 'Severe'

df['pollution_level'] = df['pollution_index'].apply(classify_pollution)


scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[['pm25', 'no2', 'co']])

kmeans = KMeans(n_clusters=4, random_state=42)
df['cluster'] = kmeans.fit_predict(X_scaled)


cluster_summary = df.groupby('cluster')[['pm25', 'no2', 'co', 'pollution_index']].mean().round(1)
print("Cluster Summary:\n", cluster_summary, "\n")


cluster_names = {
    0: 'Low Pollution',
    1: 'Moderate Pollution',
    2: 'High CO Dominant',
    3: 'Severe PM2.5 Hotspot'
}

df['cluster_label'] = df['cluster'].map(cluster_names)


final_columns = [
    'city', 'pm25', 'no2', 'co', 'pollution_index',
    'pollution_level', 'cluster', 'cluster_label'
]
df = df[final_columns]


output_path = "data/Final_Pollution_Hotspot_Dataset.csv"
df.to_csv(output_path, index=False)

print(f" Final dataset ready! Saved to {output_path}")
print(f" Total cities: {df['city'].nunique()}")
print(f"Columns: {list(df.columns)}")




import pandas as pd

df = pd.read_csv("data/India_Daily_AirQuality_2021_2026.csv")
cities = sorted(df['city'].unique())
print(f" Found {len(cities)} unique cities")
pd.DataFrame(cities, columns=['city']).to_csv("data/Unique_Cities.csv", index=False)
print(" Saved unique city list to data/Unique_Cities.csv")

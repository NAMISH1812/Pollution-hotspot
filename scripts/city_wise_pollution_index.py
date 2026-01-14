import pandas as pd
df = pd.read_csv("data/India_Daily_AirQuality_2021_2026.csv")
df_clean = df[(df['pm25'] > 0) & (df['no2'] > 0) & (df['co'] > 0)]

city_summary = (
    df_clean.groupby('city')[['pm25','no2','co']]
    .mean()
    .sort_values('pm25', ascending=False)
)

city_summary['pollution_index'] = (
    0.3 * city_summary['pm25'] +
    0.2* city_summary['no2'] +
    0.5 * city_summary['co']
)

city_summary = city_summary.sort_values('pollution_index', ascending=False)
city_summary.to_csv("data/City_Wise_Pollution_Index.csv")


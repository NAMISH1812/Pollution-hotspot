import pandas as pd
df = pd.read_csv("data/India_AirQuality_2021_2026.csv")

df.columns = df.columns.str.lower()


df.rename(columns={
    'pollutant': 'parameter',
    'measurement': 'value',
    'timestamp': 'datetime'
}, inplace=True)


df = df.dropna(subset=['city', 'latitude', 'longitude', 'value'])


df['datetime'] = pd.to_datetime(df['datetime'])
df['date'] = df['datetime'].dt.date
df_daily = (
    df.groupby(['city', 'parameter', 'date'], as_index=False)
      .agg({'value':'mean','latitude':'first','longitude':'first'})
)
df_daily.head()
df_wide = df_daily.pivot_table(
    index=['city','date','latitude','longitude'],
    columns='parameter',
    values='value'
).reset_index()
df_wide[['pm25','no2','co']] = (
    df_wide.groupby('city')[['pm25','no2','co']]
    .transform(lambda x: x.fillna(x.mean()))
)

df_wide.to_csv("India_Daily_AirQuality_2021_2026.csv", index=False)
print(" Saved: India_Daily_AirQuality_2021_2026.csv")




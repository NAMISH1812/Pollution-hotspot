import pandas as pd
import numpy as np


df = pd.read_csv("data/City_Wise_Pollution_Index.csv")


df = df[['city','pm25','no2','co']]


df['pollution_index'] = (
    0.4 * df['pm25'] +
    0.2 * df['no2'] +
    0.4 * df['co']
)


def classify_aqi(pi):
    if pi <= 50:
        return 'Good'
    elif pi <= 100:
        return 'Moderate'
    elif pi <= 150:
        return 'Poor'
    elif pi <= 250:
        return 'Very Poor'
    else:
        return 'Severe'

df['Pollution_Level'] = df['pollution_index'].apply(classify_aqi)




df.to_csv("data/India_AirQuality_Featured.csv", index=False)
print(" City-level feature engineering complete.")

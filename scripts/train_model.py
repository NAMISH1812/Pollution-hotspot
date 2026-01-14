
import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report


df = pd.read_csv("data/Final_Pollution_Hotspot_Dataset.csv")


le = LabelEncoder()
df['pollution_level_encoded'] = le.fit_transform(df['pollution_level'])


X = df[['pm25', 'no2', 'co']]
y = df['pollution_level_encoded']


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = RandomForestClassifier(n_estimators=200, max_depth=5, random_state=42)
model.fit(X_train, y_train)


print(" Model trained successfully!")
print(" Classification Report:")
print(classification_report(
    y_test,
    model.predict(X_test),
    labels=np.unique(y),  
    target_names=le.classes_
))



joblib.dump(model, "models/pollution_rf_model.pkl")
joblib.dump(le, "models/label_encoder.pkl")
print(" Model and encoder saved to /models/")
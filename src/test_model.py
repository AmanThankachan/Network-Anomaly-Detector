import pandas as pd
import joblib
from sklearn.metrics import classification_report

# Load preprocessed data and model
features = pd.read_csv('features_scaled.csv')
labels = pd.read_csv('labels.csv')
model = joblib.load('anomaly_model.pkl')

# Predict anomalies
predictions = model.predict(features)
predictions = [1 if p == -1 else 0 for p in predictions]  # Convert to binary labels

# Evaluate the model
print(classification_report(labels, predictions))

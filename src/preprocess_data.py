import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

# Load dataset
data = pd.read_csv('../data/network_traffic.csv')

# Data cleaning and preprocessing
data = data.dropna()  # Remove missing values
features = data.drop('label', axis=1)  # Features
labels = data['label']  # Labels

# Standardize the features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Save preprocessed data and scaler
pd.DataFrame(features_scaled).to_csv('features_scaled.csv', index=False)
labels.to_csv('labels.csv', index=False)
joblib.dump(scaler, 'scaler.pkl')

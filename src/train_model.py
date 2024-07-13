import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# Load preprocessed data
features = pd.read_csv('features_scaled.csv')

# Train Isolation Forest model
model = IsolationForest(n_estimators=100, contamination=0.01)
model.fit(features)

# Save the trained model
joblib.dump(model, 'anomaly_model.pkl')

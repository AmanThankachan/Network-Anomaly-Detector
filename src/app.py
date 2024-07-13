from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load('anomaly_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = scaler.transform([data['features']])
    prediction = model.predict(features)
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)

# Load the pre-trained ML model
with open('water_quality_model.pkl', "rb") as f:
    model = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract values from form data
    pH = float(request.form['pH'])
    Temperature_C = float(request.form['Temperature_C'])
    Turbidity_NTU = float(request.form['Turbidity_NTU'])
    Dissolved_Oxygen_mgL = float(request.form['Dissolved_Oxygen_mgL'])
    Conductivity_uScm = float(request.form['Conductivity_uScm'])
    
    # Create features array
    features = np.array([[pH, Temperature_C, Turbidity_NTU, Dissolved_Oxygen_mgL, Conductivity_uScm]])
    
    # Make prediction using the loaded model
    prediction = model.predict(features)
    
    # Return result to the web page
    return render_template('index.html', prediction=prediction[0])  # Return JSON response for prediction
    return jsonify({'prediction': prediction[0]})

@app.route('/simulate_sensors', methods=['POST'])
def simulate_sensors():
    # Simulate sensor data
    data = {
        "pH": round(random.uniform(6.0, 9.0), 2),
        "Temperature_C": round(random.uniform(15, 35), 2),
        "Turbidity_NTU": round(random.uniform(0.2, 20.0), 2),
        "Dissolved_Oxygen_mgL": round(random.uniform(4.0, 10.0), 2),
        "Conductivity_uScm": random.randint(100, 1000)
    }

    # Prepare features array
features = np.array([[data['pH'], data['Temperature_C'], data['Turbidity_NTU'], data['Dissolved_Oxygen_mgL'], data['Conductivity_uScm']]])

# Make prediction
prediction = model.predict(features)

# Return both simulated data and prediction
return jsonify({'prediction': prediction[0], 'data': data})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
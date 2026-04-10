import os
import pickle
import numpy as np
from flask import Flask, request, render_template

app = Flask(__name__)

base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, 'crop_yield_model.pkl')

try:
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    print("✅ Model loaded successfully")
except Exception as e:
    model = None
    print(f"❌ Error loading model: {e}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return render_template('index.html', prediction_text="Error: Model file not found.")

    try:
        n = float(request.form.get('Nitrogen', 0))
        p = float(request.form.get('Phosphorus', 0))
        k = float(request.form.get('Potassium', 0))
        temp = float(request.form.get('Temperature', 0))
        ph = float(request.form.get('pH', 0))
        rain = float(request.form.get('Rainfall', 0))

        final_features = np.zeros(42)
        final_features[0] = n      # N
        final_features[1] = p      # P
        final_features[2] = k      # K
        final_features[3] = rain   # Rainfall 
        final_features[4] = temp   # Temperature 
        final_features[5] = ph     # Soil_pH 
        
        final_features[6] = 2024   # Year
        final_features[7] = (n + p + k) / 3  # NPK Index
        final_features[8] = (temp + rain) / 500 # Climate Index
        final_features[9] = ph / 7 # Soil Health Index

        # Prediction
        prediction = model.predict([final_features])[0]
        output = round(prediction, 1)

        return render_template('index.html', 
                               prediction_text=f'Predicted Yield: {output} kg/acre',
                               n_val=n, p_val=p, k_val=k, temp_val=temp, ph_val=ph, rain_val=rain)

    except Exception as e:
        print(f"Error: {e}")
        return render_template('index.html', prediction_text="Error in calculation")

if __name__ == "__main__":
    app.run(debug=True)
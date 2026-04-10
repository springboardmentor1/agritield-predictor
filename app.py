import os
import pickle
import numpy as np
from flask import Flask, request, render_template

# 1. ആദ്യം ആപ്പ് ഡിഫൈൻ ചെയ്യണം (ഇതാണ് വിട്ടുപോയത്)
app = Flask(__name__)

# 2. മോഡൽ ലോഡ് ചെയ്യുന്ന ലോജിക്
base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, 'crop_yield_model.pkl')

try:
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    print("✅ Model loaded successfully")
except Exception as e:
    model = None
    print(f"❌ Error loading model: {e}")

# 3. ഹോം പേജ് റൂട്ട്
@app.route('/')
def home():
    return render_template('index.html')

# 4. പ്രെഡിക്റ്റ് റൂട്ട്
@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return render_template('index.html', prediction_text="Error: Model file not found.")

    try:
        # ഫോമിൽ നിന്നുള്ള വാല്യൂസ്
        n = float(request.form.get('Nitrogen', 0))
        p = float(request.form.get('Phosphorus', 0))
        k = float(request.form.get('Potassium', 0))
        temp = float(request.form.get('Temperature', 0))
        ph = float(request.form.get('pH', 0))
        rain = float(request.form.get('Rainfall', 0))

        # 42 ഫീച്ചറുകൾ ഉള്ള ലിസ്റ്റ്
        final_features = np.zeros(42)
        
        # ശരിയായ ക്രമത്തിൽ വാല്യൂസ് നൽകുന്നു
        final_features[0] = n      # N
        final_features[1] = p      # P
        final_features[2] = k      # K
        final_features[3] = rain   # Rainfall (നിങ്ങളുടെ മോഡൽ അനുസരിച്ച് 4-ാമത്തെ കോളം)
        final_features[4] = temp   # Temperature (5-ാമത്തെ കോളം)
        final_features[5] = ph     # Soil_pH (6-ാമത്തെ കോളം)
        
        # മറ്റ് നിർണ്ണായക കോളങ്ങൾ (Year and Indexes)
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

# 5. ആപ്പ് റൺ ചെയ്യുന്നു
if __name__ == "__main__":
    app.run(debug=True)
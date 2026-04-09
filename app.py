from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load model
model = joblib.load("crop_yield_model.pkl")
print("Model expects:", model.n_features_in_)   
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        N = float(request.form['N'])
        P = float(request.form['P'])
        K = float(request.form['K'])
        rainfall = float(request.form['rainfall'])
        temperature = float(request.form['temperature'])
        ph = float(request.form['ph'])
        year = float(request.form['year'])

        input_data = np.array([[N, P, K, rainfall, temperature, ph, year]])

        prediction = model.predict(input_data)

        return render_template('index.html', prediction_text=f"Predicted Yield: {prediction[0]:.2f} kg/acre")

    except Exception as e:
        print("ERROR:", e)  
        return render_template('index.html', prediction_text="Error in input")

if __name__ == "__main__":
    app.run(debug=True)
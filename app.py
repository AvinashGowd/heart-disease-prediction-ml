from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np
import os

app = Flask(__name__)

# Load the model
model_path = 'model.pkl'
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    model = None
    print("Warning: model.pkl not found. Please ensure the model file is in the project directory.")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if not model:
        return render_template('index.html', prediction_text="Model not loaded.")

    try:
        # Extract features from form and create a DataFrame
        # Using a DataFrame ensures feature names match if the model was trained with them
        features_dict = {
            'age': [float(request.form['age'])],
            'cp': [float(request.form['cp'])],
            'trestbps': [float(request.form['trestbps'])],
            'chol': [float(request.form['chol'])],
            'thalach': [float(request.form['thalach'])],
            'exang': [float(request.form['exang'])],
            'oldpeak': [float(request.form['oldpeak'])],
            'ca': [float(request.form['ca'])],
            'thal': [float(request.form['thal'])]
        }
        
        final_features = pd.DataFrame(features_dict)
        
        # Predict
        prediction = model.predict(final_features)
        
        # Get Probability
        if hasattr(model, "predict_proba"):
            prediction_proba = model.predict_proba(final_features)
            probability = np.round(prediction_proba[0][1] * 100, 2)
            prob_text = f"{probability}%"
        else:
            probability = None
            prob_text = ""

        output = prediction[0]
        
        if output == 1:
            res_text = "High Chance of Heart Disease"
            css_class = "danger"
        else:
            res_text = "Low Chance of Heart Disease"
            css_class = "safe"

        return render_template('index.html', prediction_text=res_text, prediction_prob=prob_text, prediction_class=css_class)

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}", prediction_class="error")

if __name__ == "__main__":
    app.run(debug=True)

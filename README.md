# Heart Disease Prediction Web Application

This is a machine learning-based web application that predicts the likelihood of heart disease based on medical attributes. Built with Flask and a pre-trained Scikit-Learn pipeline model.

## Features

- **Interactive Web Interface**: Modern, responsive UI with a clean design.
- **Real-time Prediction**: Instantly predicts heart disease risk (Low/Medium/High) along with a probability score.
- **User Guidance**: Tooltips for every input field to guide users on what to enter.
- **Visual Feedback**: Loading animations and color-coded results.
- **Pre-trained Model**: Uses a robust machine learning pipeline saved as `model.pkl`.

## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS (Custom styling with gradients and animations)
- **Machine Learning**: Scikit-Learn, Joblib, Pandas, NumPy

## Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/AvinashGowd/heart-disease-prediction-ml.git
    cd heart-disease-prediction-ml
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application**:
    ```bash
    python app.py
    ```

4.  **Access the app**:
    Open your browser and go to `http://127.0.0.1:5000`.

## Usage

Fill in the 9 medical details in the form:
1.  **Age**: Age in years.
2.  **Chest Pain Type (cp)**: 0-3.
3.  **Resting Blood Pressure (trestbps)**: mm Hg.
4.  **Cholesterol (chol)**: mg/dl.
5.  **Max Heart Rate (thalach)**.
6.  **Exercise Induced Angina (exang)**: 0 or 1.
7.  **ST Depression (oldpeak)**: Numeric value.
8.  **Major Vessels (ca)**: 0-3.
9.  **Thalassemia (thal)**: 0-3.

Click **Predict Risk** to see the result.

## Project Structure

```
├── app.py              # Flask application entry point
├── model.pkl           # Pre-trained machine learning model
├── requirements.txt    # Python dependencies
├── static/
│   ├── style.css       # Custom CSS styles
│   └── images/         # Background images
└── templates/
    └── index.html      # HTML template
```

import streamlit as st
import joblib
import numpy as np

# Load the saved model
model = joblib.load('model.sav')

# Set up the app title and description
st.title("Advertising Sales Prediction App")
st.write("Enter your advertising budgets below to predict estimated Sales.")

# Create input fields for features
tv = st.number_input("TV Advertising Budget ($)", min_value=0.0, value=100.0, step=1.0)
radio = st.number_input("Radio Advertising Budget ($)", min_value=0.0, value=20.0, step=1.0)
newspaper = st.number_input("Newspaper Advertising Budget ($)", min_value=0.0, value=20.0, step=1.0)

# Predict button
if st.button("Predict Sales"):
    features = np.array([[tv, radio, newspaper]])
    prediction = model.predict(features)
    st.success(f"Predicted Sales: {prediction[0]:.2f} units")

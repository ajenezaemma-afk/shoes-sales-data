import numpy as np
import streamlit as st
import pickle
import os

# Get path of the model relative to this app.py file
MODEL_PATH = os.path.join(os.path.dirname(__file__), "shoes_sales_data.sav")

# Load the trained model
with open(MODEL_PATH, 'rb') as file:
    model = pickle.load(file)

# Streamlit UI
st.title("Shoes Sales Data Prediction")
st.write("Fill the following information to get a prediction:")

# User Inputs
brand = st.number_input("Brand", value=26)
color = st.number_input("Color", value=4)
size = st.number_input("Size", value=6.5)

# Prediction on button click
if st.button("Predict"):
    # Create input in correct order and shape
    Input = np.array([[brand, color, size]])
    
    # Predict
    prediction = model.predict(Input)
    
    # Show result
    st.success(f"Predicted shoe price: {prediction[0]:.2f}")

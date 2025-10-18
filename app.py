


import numpy as np
import streamlit as st
import pickle

with open(r"C:/Users/HOME-PC/Desktop/shoes data/shoes_sales_data.sav", 'rb') as file:
    model = pickle.load(file)
    
# Load the trained model
##with open('cancer_patient_prediction_data.sav', 'rb') as file:
   ## model = pickle.load(file)

# Streamlit UI
st.title("shoes sales data prediction")
st.write("Fill the following information to get a prediction:")

# User Inputs
brand = st.number_input("brand", value=26)
color = st.number_input("color", value=4)
size = st.number_input("size", value=6.5)




# Prediction on button click
if st.button("Predict"):
    # Create input in correct order and shape
    Input = np.array([[brand,color,size]])
    
    # Predict
    prediction = model.predict(Input)
    
    # Show result
    st.success(f"shoes sales data prediction is : {prediction[0]:.2f}")


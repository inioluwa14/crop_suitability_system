import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load trained model
model_filename = "./light_gradient_boosting_model.pkl"
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

# Load LabelEncoder
encoder_filename = "label_encoder.pkl"  # Save this when encoding labels
with open(encoder_filename, "rb") as file:
    label_encoder = pickle.load(file)

# Streamlit app title
st.title("🌱 Crop Suitability Prediction System")

# Insert image
st.image("./crop_field.jpg")

# User input fields for soil and climate conditions
st.header("Enter Soil and Climate Conditions")

Nitrogen = st.number_input("Nitrogen Content (kg/ha)", min_value=0.0, step=0.1)
Phosphorus = st.number_input("Phosphorus Content (kg/ha)", min_value=0.0, step=0.1)
Potassium = st.number_input("Potassium Content (kg/ha)", min_value=0.0, step=0.1)
temperature = st.number_input("Temperature (°C)", min_value=-10.0, max_value=50.0, step=0.1)
humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, step=0.1)
ph = st.number_input("Soil pH", min_value=3.0, max_value=10.0, step=0.1)
rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=1000.0, step=0.1)

# Predict function
def predict_crop():
    input_data = np.array([[Nitrogen, Phosphorus, Potassium, temperature, humidity, ph, rainfall]])
    #Get probability for each class
    numeric_prediction = model.predict_proba(input_data)[0]

    #Get the top 3 crop indices with the higest probabilities
    top_3_indices = np.argsort(numeric_prediction)[-3:][::-1] #Sort this is descending order

    #convert the indices to their crop names
    crop_name = label_encoder.inverse_transform(top_3_indices.flatten()) # Convert number back to crop name
    probabilities = numeric_prediction[top_3_indices]
    # return crop_name
    
    return list(zip(crop_name, probabilities))

# Prediction button
if st.button("Predict Crop"):
    recommended_crops = predict_crop()

    st.subheader("🌾 Top 3 Recommended Crops")

    for crop, prob in recommended_crops:
        st.success(f"✅ **{crop.upper()}** ({prob*100:.2f}% suitability)")

    # st.success(f"Recommended Crop: {recommended_crop.upper()}")

# Information about the project
st.markdown("### About the Project")
st.write(
    "This system predicts the top 3 suitable crops for the agricultural field based on soil and climate conditions using a trained machine learning model. "
    "It helps farmers optimize their agricultural productivity by providing data-driven insights."
)

import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("house_price_model.pkl")

st.title("🏠 House Price Prediction App")
st.write("Enter property details to estimate the sale price.")

# User inputs
sq_ft = st.number_input("Living Area (GrLivArea in sq ft)", min_value=500, max_value=6000, value=1500)
bedrooms = st.number_input("Number of Bedrooms (BedroomAbvGr)", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("Number of Bathrooms (FullBath)", min_value=1, max_value=5, value=2)

if st.button("Predict Price"):
    # Prepare input data
    input_data = pd.DataFrame([[sq_ft, bedrooms, bathrooms]], 
                               columns=["GrLivArea", "BedroomAbvGr", "FullBath"])
    
    # Predict
    prediction = model.predict(input_data)[0]
    
    st.success(f"Estimated Sale Price: ${prediction:,.2f}")
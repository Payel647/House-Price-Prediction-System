import streamlit as st
import pandas as pd
import joblib

model = joblib.load("house_price_model.pkl")

st.title("🏠 House Price Prediction App")

lot_area = st.number_input("Lot Area")
overall_cond = st.slider("Overall Condition", 1, 10)
year_built = st.number_input("Year Built")

if st.button("Predict Price"):
    input_df = pd.DataFrame([{
        "LotArea": lot_area,
        "OverallCond": overall_cond,
        "YearBuilt": year_built
    }])

    price = model.predict(input_df)
    st.success(f"Predicted Price: ₹ {price[0]:,.2f}")

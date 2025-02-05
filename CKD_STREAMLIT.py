import streamlit as st
import joblib
import pandas as pd

# LOAD THE TRAINED MODEL
MODEL_PATH = r"CKD SAVED MODEL.pkl"  
with open(MODEL_PATH, "rb") as file:
    model = joblib.load(file)

# ADD TITLE TO THE APP
st.title("🏥 Chronic Kidney Disease Prediction")

# CREATING INPUT BOX
bp = st.number_input("Blood Pressure", min_value=50, max_value=200, value=120)
sg = st.number_input("Specific Gravity", min_value=1.000, max_value=1.030, value=1.010, format="%.3f")
al = st.number_input("Albumin", min_value=0, max_value=5, value=1)
su = st.number_input("Sugar", min_value=0, max_value=5, value=0)
sc = st.number_input("Serum Creatinine", min_value=0.0, max_value=10.0, value=1.2)
sod = st.number_input("Sodium", min_value=100, max_value=160, value=137)
pot = st.number_input("Potassium", min_value=2.0, max_value=10.0, value=4.5)

#CREATE PREDICT BUTTON AND PREDICT THE OUTPUT USING THE TRAINED MODEL
if st.button("Predict"):
    input_data = pd.DataFrame([[bp, sg, al, su, sc, sod, pot]],
                              columns=["Blood Pressure", "Specific Gravity", "Albumin", "Sugar", "Serum Creatinine", "Sodium", "Potassium"])
    prediction = model.predict(input_data)
    result = "Patient has CKD" if prediction[0] == 1 else "No CKD detected"
    st.subheader("Prediction Result:")
    st.write(f"### {result}")

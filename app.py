import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Student Performance Predictor")

st.title("Student Performance Prediction")

model = joblib.load("model.pkl")

with st.form("prediction_form"):
    hours = st.number_input("Hours Studied", 0, 50, 10)
    attendance = st.slider("Attendance (%)", 0, 100, 75)
    sleep = st.slider("Sleep Hours", 0, 12, 7)
    prev = st.slider("Previous Scores", 0, 100, 70)
    tutor = st.number_input("Tutoring Sessions", 0, 10, 1)
    activity = st.slider("Physical Activity", 0, 10, 3)

    gender = st.selectbox("Gender", ["Male", "Female"])
    school = st.selectbox("School Type", ["Public", "Private"])
    parent = st.selectbox("Parental Involvement", ["Low", "Medium", "High"])
    internet = st.selectbox("Internet Access", ["Yes", "No"])
    motivation = st.selectbox("Motivation Level", ["Low", "Medium", "High"])

    submitted = st.form_submit_button("Predict")

if submitted:
    input_df = pd.DataFrame([{
        "Hours_Studied": hours,
        "Attendance": attendance,
        "Sleep_Hours": sleep,
        "Previous_Scores": prev,
        "Tutoring_Sessions": tutor,
        "Physical_Activity": activity,
        "Gender_encoded": gender,
        "School_Type_encoded": school,
        "Parental_Involvement_encoded": parent,
        "Internet_Access_encoded": internet,
        "Motivation_Level_encoded": motivation
    }])

    st.write("Input used:")
    st.write(input_df)

    prediction = model.predict(input_df)
    st.success(f" Predicted Exam Score: **{prediction[0]:.2f}**")

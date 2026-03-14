import streamlit as st
import joblib
import numpy as np
import os

model_path = os.path.join("Avionics", "data", "src", "anomaly_model.pkl")
model = joblib.load(model_path)
st.title("Avionics Intern Performance Consistency Analyzer")
st.write("Enter intern performance metrics to evaluate consistency and detect malpractice.")

completion_time = st.number_input("Completion Time", min_value=0.0)
errors_count = st.number_input("Errors Count", min_value=0.0)
safety_violations = st.number_input("Safety Violations", min_value=0.0)
test_cases_passed = st.number_input("Test Cases Passed", min_value=0.0)
code_complexity = st.number_input("Code Complexity (1-15)", min_value=1.0, max_value=15.0)
review_score = st.number_input("Review Score", min_value=0.0)

if st.button("Evaluate"):
    features = np.array([[completion_time,
                          errors_count,
                          safety_violations,
                          test_cases_passed,
                          code_complexity,
                          review_score]])

    prediction = model.predict(features)

    st.subheader("Evaluation Result")

    if prediction[0] == -1:
        st.error(" MALPRACTICE DETECTED")
        st.write("The performance appears inconsistent and may indicate unsafe practices.")
    else:
        st.success(" NO MALPRACTICE DETECTED")
        st.write("The intern performance appears consistent.")

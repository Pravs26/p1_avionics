import joblib
import os
import numpy as np

MODEL_PATH = os.path.join(os.path.dirname(__file__), "anomaly_model.pkl")

def predict_anomaly(data):
    model = joblib.load(MODEL_PATH)
    features = np.array([[
        data["completion_time"],
        data["errors_count"],
        data["safety_violations"],
        data["test_cases_passed"],
        data["code_complexity"],
        data["review_score"]
    ]])

    result = model.predict(features)[0]
    return "MALPRACTICE DETECTED" if result == -1 else "NO MALPRACTICE DETECTED"

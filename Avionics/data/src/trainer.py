import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
import os

def train_model():
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "avionics_intern_performance.csv")

    data = pd.read_csv(file_path)
    X = data.drop(columns=["candidate_id", "task_id"])
    model = IsolationForest(contamination=0.25, random_state=42)
    model.fit(X)
    model_path = os.path.join(base_path, "anomaly_model.pkl")
    joblib.dump(model, model_path)

    print("\nModel trained successfully!")
    print("Model saved at:", model_path)
if __name__ == "__main__":
    train_model()

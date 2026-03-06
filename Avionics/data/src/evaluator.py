import pandas as pd
import os
from anomaly_model import predict_anomaly


# ---------- Percentage Calculation ----------
def calculate_percentage(data):

    score = (
        (100 - data["completion_time"]) * 0.20 +
        (100 - data["errors_count"] * 10) * 0.20 +
        (100 - data["safety_violations"] * 15) * 0.20 +
        (data["test_cases_passed"]) * 0.25 +
        (data["review_score"] * 10) * 0.15
    )

    return round(score, 2)


# ---------- Score based status ----------
def get_score_status(score):

    if score >= 75:
        return "GOOD TO GO"
    elif score >= 50:
        return "MORE PRACTICE NEEDED"
    else:
        return "REVIEW REQUIRED"



# ---------- ML + Score combined decision ----------
def get_final_status(score, data):

    # ML malpractice detection (single detector)
    malpractice = predict_anomaly(data)

    # academic status
    if score >= 85:
        status = "GOOD TO GO"
    elif score >= 60:
        status = "REVIEW REQUIRED"
    else:
        status = "MORE PRACTICE NEEDED"

    return status, malpractice


    # ML has higher priority than marks
    if anomaly:
        return "REVIEW REQUIRED"

    return get_score_status(score)


# ---------- Historical comparison ----------
def malpractice_check(current_score):

    base = os.path.dirname(__file__)
    dataset = pd.read_csv(os.path.join(base, "avionics_intern_performance.csv"))

    historical_scores = []

    for _, row in dataset.iterrows():
        s = calculate_percentage(row)
        historical_scores.append(s)

    avg_history = sum(historical_scores) / len(historical_scores)

    difference = current_score - avg_history

    if difference <= 20:
        result = "NO MALPRACTICE DETECTED"
    elif difference <= 40:
        result = "SUSPICIOUS PERFORMANCE JUMP"
    else:
        result = "POSSIBLE MALPRACTICE"

    return round(avg_history, 2), result


# ---------- Main Evaluation Function ----------
def run_evaluation(return_inputs=False):


    print("\nEnter Student Marks\n")

    data = {
    "completion_time": float(input("Completion Time: ")),
    "errors_count": float(input("Errors Count: ")),
    "safety_violations": float(input("Safety Violations: ")),
    "test_cases_passed": float(input("Test Cases Passed: ")),
    "code_complexity": float(input("Code Complexity (1-15): ")),
    "review_score": float(input("Review Score: "))
}


    percentage = calculate_percentage(data)
    status = get_final_status(percentage, data)
    avg_history, malpractice = malpractice_check(percentage)

    if return_inputs:
       return percentage, status, avg_history, malpractice, data
    else:
       return percentage, status, avg_history, malpractice



# ---------- Standalone Run ----------
if __name__ == "__main__":
    p, s, avg, m = run_evaluation()

    print("\nMarks Percentage :", p, "%")
    print("Status :", s)
    print("Historical Average :", avg, "%")
    print("Malpractice :", m)

import pandas as pd
import numpy as np

rows = []

for i in range(800):

    completion_time = np.random.randint(20, 200)
    errors_count = np.random.randint(0, 15)
    safety_violations = np.random.randint(0, 8)

    # LOGICAL RELATIONSHIP
    performance_factor = max(0, 100 - (errors_count*4 + safety_violations*6))

    test_cases_passed = np.random.randint(performance_factor-10, performance_factor+5)
    test_cases_passed = max(0, min(100, test_cases_passed))

    code_complexity = np.random.randint(5, 15)

    review_score = round((test_cases_passed/10) + np.random.uniform(-1,1), 2)
    review_score = max(0, min(10, review_score))

    rows.append([
        f"CAND_{np.random.randint(1,50)}",
        f"TASK_{np.random.randint(1,20)}",
        completion_time,
        errors_count,
        safety_violations,
        test_cases_passed,
        code_complexity,
        review_score
    ])

columns = [
    "candidate_id","task_id","completion_time","errors_count",
    "safety_violations","test_cases_passed","code_complexity","review_score"
]

df = pd.DataFrame(rows, columns=columns)
df.to_csv("avionics_intern_performance.csv", index=False)

print("Clean logical dataset generated!")


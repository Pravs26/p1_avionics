# Avionics Intern Performance Consistency Analyzer
## Problem Statement

In avionics systems, consistency is critical for ensuring safety and reliability. Even small inconsistencies in software development can lead to unsafe system behavior.
This project aims to detect inconsistent task performance by internship candidates that may indicate weak conceptual understanding, unsafe coding practices, or irregular work patterns. By identifying such inconsistencies early, the system helps maintain the high safety and reliability standards required in avionics software development.

## Project Overview

The Avionics Intern Performance Consistency Analyzer is a Python-based analytical system designed to evaluate intern task performance using deterministic checks and anomaly detection techniques.
The system analyzes performance metrics such as task completion time, errors count, safety violations, test cases passed, code complexity, and review scores. Using these metrics, it determines whether the intern’s performance is consistent, requires improvement, or indicates potential malpractice.
The project ensures that the same input produces the same output across multiple runs, verifying system determinism — an essential property in avionics systems.

## How the Project Works

The user enters performance metrics for a specific intern task.
The system evaluates the input using predefined scoring logic.
A machine learning anomaly detection model analyzes the performance metrics.
The system performs a determinism check by running the evaluation multiple times.
Results are displayed in a structured table including:
Run number
Marks percentage
Status of the intern
The system also checks whether malpractice or abnormal performance patterns are detected.

## Solution

The proposed solution combines deterministic evaluation logic with machine learning-based anomaly detection.

## Key components include:

1. Deterministic evaluation system to ensure consistent outputs.
2. Isolation Forest based anomaly detection model.
3. Real-time performance evaluation based on intern input.
4. Automated malpractice detection based on unusual metric combinations.
5. Tabular result display for easy interpretation.
This approach ensures reliable evaluation while maintaining the safety standards expected in avionics environments.

## Tech Stack Used

The project is implemented using the following technologies:

1. Python
2. NumPy
3. Pandas
4. Scikit-learn
5. Joblib
6. VS Code
7. Git
8. GitHub

## Implementation

The project consists of multiple modules that work together to analyze intern performance.

## Main Components:

1. Data Generation Module
Generates structured training data for model training.

2. Feature Extraction Module
Extracts relevant features from performance metrics.

3. Anomaly Detection Model
Uses Isolation Forest to detect abnormal patterns.

4. Trainer Module
Trains the anomaly detection model using historical data.

5. Evaluator Module
Processes user inputs and calculates performance scores.

6. Determinism Checker
Ensures that identical inputs always produce identical outputs across multiple runs.

## Conclusion

This project demonstrates how deterministic evaluation and machine learning-based anomaly detection can be used together to analyze intern task performance in safety-critical environments such as avionics.
The system helps identify inconsistent performance, potential malpractice, and areas where interns may require additional practice or review. By ensuring output consistency and automated anomaly detection, the project contributes to improving reliability and safety in software development processes.

## Project Links
GitHub Repository
https://github.com/Pravs26/p1_avionics.git

Deployment Link
https://p1avionics-ustdkncs6l9jxmmyzdnvs7.streamlit.app/

Author
K. SAI PRAVALLIKA

LinkedIn Profile
https://www.linkedin.com/in/sai-pravallika-kovvuri-9b289b376

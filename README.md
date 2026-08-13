# AI Cybersecurity Intrusion Detection

A machine-learning project demonstrating how network-traffic features can be used to classify events as **normal** or potential **intrusion**.

## Objective
The project demonstrates supervised machine learning for a cybersecurity classification task.

Features:
- Packet rate
- Connection duration
- Failed login attempts
- Bytes per second

Target:
- `0` — Normal traffic
- `1` — Potential intrusion

## Technologies
- Python
- Pandas
- Scikit-learn
- Logistic Regression
- StandardScaler
- Machine Learning
- Cybersecurity

## Methodology
1. Prepare network-traffic data.
2. Split features and labels.
3. Create training and testing sets.
4. Standardize numerical features.
5. Train a Logistic Regression classifier.
6. Evaluate classification performance.
7. Classify a new network event.

## Run
```bash
pip install -r requirements.txt
python train.py
```

## Important Note
The dataset is **synthetic** and intended for educational and portfolio demonstration only. It is not a production intrusion-detection system.

## Future Improvements
- Use a real public intrusion-detection dataset.
- Compare Random Forest, SVM, and neural networks.
- Address class imbalance.
- Add precision, recall, F1-score and ROC-AUC.
- Build a real-time monitoring pipeline.
- Investigate lightweight models for efficient edge-based intrusion detection.

## Author
**Abdulhamid Ibrahim Mustapha**

MSc Information Systems | BSc Information Technology

Research interests: Artificial Intelligence, Machine Learning, Cybersecurity, Efficient AI Systems, and Information Systems.

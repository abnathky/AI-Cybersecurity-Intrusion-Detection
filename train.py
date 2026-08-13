import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Synthetic network-traffic dataset for an educational portfolio project.
data = {
    "packet_rate": [20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,22,28,33,38,43,48,53,58,63,68,73,78,83,88,93,98,103,108,113,118],
    "connection_duration": [90,85,80,75,70,65,60,55,50,45,40,35,30,25,20,18,15,12,10,8,88,82,77,72,67,62,57,52,47,42,37,32,27,22,17,16,13,11,9,7],
    "failed_logins": [0,0,1,0,1,1,0,1,2,1,2,2,3,3,4,4,5,6,6,7,0,1,0,1,1,0,1,2,1,2,2,3,3,4,4,5,6,7,7,8],
    "bytes_per_second": [120,130,125,140,150,145,160,155,170,180,190,200,210,220,230,240,250,260,270,280,125,135,130,145,155,150,165,160,175,185,195,205,215,225,235,245,255,265,275,285],
    "intrusion": [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1]
}

df = pd.DataFrame(data)
X = df.drop("intrusion", axis=1)
y = df["intrusion"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

model = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression(max_iter=1000, random_state=42))
])

model.fit(X_train, y_train)
predictions = model.predict(X_test)

print("AI Cybersecurity Intrusion Detection")
print("-" * 40)
print(f"Accuracy: {accuracy_score(y_test, predictions):.2%}")
print("\nClassification Report:")
print(classification_report(y_test, predictions, target_names=["Normal", "Intrusion"]))

new_event = pd.DataFrame([{
    "packet_rate": 100,
    "connection_duration": 12,
    "failed_logins": 6,
    "bytes_per_second": 260
}])

result = model.predict(new_event)[0]
print("\nExample event classification:", "Intrusion" if result else "Normal")

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import joblib

df = pd.read_csv("data/machine_failure.csv")

X = df.drop(columns=["machine_failure"])
y = df["machine_failure"]

# model = RandomForestClassifier()
# model.fit(X, y)

# print("Model trained successfully.")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)

print("Model trained successfully.")

joblib.dump(model, "models/machine_failure_model.pkl")


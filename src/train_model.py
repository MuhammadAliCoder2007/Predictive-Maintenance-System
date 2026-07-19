from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import joblib
from sklearn.metrics import accuracy_score

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



y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy*100:.2f}%")

joblib.dump(model, "models/machine_failure_model.pkl")

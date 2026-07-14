import joblib
model = joblib.load("models/machine_failure_model.pkl")
new_machine = [[95, 0.8, 130, 58, 2100]]
prediction = model.predict(new_machine)

print("Prediction:", prediction[0])
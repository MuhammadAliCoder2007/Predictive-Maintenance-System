import joblib
def predict(temperature, vibration, pressure, humidity, rpm):
    model = joblib.load("models/machine_failure_model.pkl")
    new_machine = [[temperature, vibration, pressure, humidity, rpm]]
    prediction = model.predict(new_machine)
    return prediction[0]
def predict_probability(temperature, vibration, pressure, humidity, rpm):
    new_machine = [[temperature, vibration, pressure, humidity, rpm]]
    return model.predict_proba(new_machine)[0][1]
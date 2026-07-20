#planning to visualize which features are most important for the model to predict the machine failure
import joblib
import pandas as pd

model = joblib.load("models/machine_failure_model.pkl")

feature_names = ["temperature","vibration","pressure","humidity","rpm"]


importance = pd.DataFrame({
    "feature": feature_names,
    "importance": model.feature_importances_*100
}).sort_values(by="importance",ascending=False)

for _, row in importance.iterrows():
    print(f"{row['feature']}: {row['importance']:.2f}%")



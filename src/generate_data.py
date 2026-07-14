import pandas as pd
import numpy as np

np.random.seed(42)

data = pd.read_csv("data/machine_failure.csv")

df = pd.DataFrame(data)


df["machine_failure"] = (
    (df["temperature"] > 90) | (df["pressure"] > 125) | (df["vibration"] > 0.8)
).astype(int)

print("Data generated successfully.")

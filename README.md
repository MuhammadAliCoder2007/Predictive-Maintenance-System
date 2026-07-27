# 🔧 Predictive Maintenance System

A machine learning web application that predicts whether an industrial machine is likely to fail based on sensor readings. The project uses a Random Forest Classifier trained on synthetic machine sensor data and provides predictions through an interactive Streamlit dashboard.

---

## 📖 Project Overview

Predictive maintenance helps identify potential equipment failures before they happen, reducing downtime and maintenance costs.

This project demonstrates an end-to-end machine learning workflow:

- Generate machine sensor data
- Train a machine learning model
- Evaluate model performance
- Save and load the trained model
- Predict machine failure
- Display predictions through a Streamlit web application

---

## 🚀 Features

- 📊 Synthetic machine sensor dataset generation
- 🤖 Random Forest machine learning model
- 📈 Model evaluation using train/test split
- 💾 Model persistence using Joblib
- ⚡ Real-time machine failure prediction
- 🎯 Prediction confidence score
- 🌐 Interactive Streamlit user interface
- 📉 Feature importance analysis

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib
- Matplotlib

---

## 📂 Project Structure

```
Predictive-Maintenance-System/
│
├── app/
│   └── app.py                 # Streamlit application
│
├── data/
│   └── machine_failure.csv    # Machine sensor dataset
│
├── images/                    # Screenshots and visualizations
│
├── models/
│   └── machine_failure_model.pkl
│
├── notebooks/
│
├── src/
│   ├── generate_data.py
│   ├── preprocess.py
│   ├── train_model.py
│   ├── predict.py
│   └── visualize.py
│
├── README.md
└── .gitignore
```

---

## 📊 Dataset

The model uses the following machine sensor readings:

| Feature | Description |
|----------|-------------|
| Temperature | Machine operating temperature (°C) |
| Vibration | Machine vibration level |
| Pressure | Internal machine pressure |
| Humidity | Environmental humidity (%) |
| RPM | Machine rotational speed |

Target:

- **0** → Machine is unlikely to fail
- **1** → Machine is likely to fail

---

## ⚙️ Machine Learning Pipeline

1. Generate synthetic machine sensor data
2. Split the dataset into training and testing sets
3. Train a Random Forest Classifier
4. Evaluate model performance
5. Save the trained model
6. Load the model for predictions
7. Display predictions through Streamlit

---

## 💻 Running the Project

### Clone the repository

```bash
git clone https://github.com/MuhammadAliCoder2007/Predictive-Maintenance-System.git
cd Predictive-Maintenance-System
```

### Install dependencies

```bash
pip install pandas numpy scikit-learn streamlit matplotlib joblib
```

### Train the model

```bash
py src/train_model.py
```

### Launch the application

```bash
py -m streamlit run app/app.py
```

---

## 📸 Application Preview

*Add screenshots of your Streamlit application here.*

Example:

```
images/app.png
```

---

## 📈 Example Prediction

Input:

| Temperature | Vibration | Pressure | Humidity | RPM |
|-------------|-----------|----------|----------|-----|
| 95 | 0.80 | 130 | 58 | 2100 |

Output:

```
⚠ Machine Status: High Failure Risk

Failure Probability: 98%
```

---

## 📌 Future Improvements

- Use real industrial maintenance datasets
- Support multiple machine learning models
- Hyperparameter tuning
- Interactive charts and dashboards
- Model explainability with SHAP
- Deploy the application online

---

## 🎯 Learning Outcomes

This project helped me gain hands-on experience with:

- Data preprocessing
- Machine learning model training
- Model evaluation
- Model persistence
- Feature importance analysis
- Streamlit application development
- Organizing a complete machine learning project

---

## 👤 Author

**Muhammad Ali**

GitHub:
https://github.com/MuhammadAliCoder2007

---

## 📄 License

This project is licensed under the MIT License.

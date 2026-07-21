import streamlit as st

from src.predict import predict

st.title("Predictive Maintenance System")
st.write("Enter machine senor readings: ")

temperature = st.number_input("Temperature (°C)", min_value=0.0)
vibration = st.number_input("Vibration", min_value=0.0)
pressure = st.number_input("Pressure", min_value=0.0)
humidity = st.number_input("Humidity (%)", min_value=0.0)
rpm = st.number_input("RPM", min_value=0)


if st.button("Predict"):
    if predict(temperature, vibration, pressure, humidity, rpm)==1:
        st.write("Machine is likely to fail")
    else:
        st.write("Machine is likely to not fail")
import numpy as np
import pandas as pd
import joblib
import streamlit as st 

model = joblib.load('waterdtc.joblib')

def predict_water_potability(ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity):
    prediction = model.predict([[ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity]])
    return prediction

def main():
    ph = float(st.text_input("ph", placeholder="Type Here"))
    hardness = float(st.text_input("Hardness", placeholder="Type Here"))
    solids = float(st.text_input("Solids", placeholder="Type Here"))
    chloramines = float(st.text_input("Chloramines", placeholder="Type Here"))
    sulfate = float(st.text_input("Sulfate", placeholder="Type Here"))
    conductivity = float(st.text_input("Conductivity", placeholder="Type Here"))
    organic_carbon = float(st.text_input("Organic_carbon", placeholder="Type Here"))
    trihalomethanes = float(st.text_input("Trihalomethanes", placeholder="Type Here"))	
    turbidity = float(st.text_input("Turbidity", placeholder="Type Here"))

    if st.button("Get Prediction"):
        output = predict_water_potability(ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity)
        st.session_state['prediction'] = output

    if 'prediction' in st.session_state:
        if st.session_state['prediction'] == 0:
            st.markdown("0", unsafe_allow_html=True)
        else:
            st.markdown("1", unsafe_allow_html=True)

if __name__ == '__main__':
    main()

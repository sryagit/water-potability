import numpy as np
import pandas as pd
import joblib
import streamlit as st 

model = joblib.load('water.joblib')

def predict_water_potability(ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity):
    prediction = model.predict([[ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity]])
    return prediction

def main():
    ph = st.text_input("ph", placeholder="Type Here") 
    hardness = st.text_input("Hardness", placeholder="Type Here")
    solids = st.text_input("Solids", placeholder="Type Here")
    chloramines = st.text_input("Chloramines", placeholder="Type Here")
    sulfate = st.text_input("Sulfate", placeholder="Type Here")
    conductivity = st.text_input("Conductivity", placeholder="Type Here")	
    organic_carbon = st.text_input("Organic_carbon", placeholder="Type Here")	
    trihalomethanes = st.text_input("Trihalomethanes", placeholder="Type Here")	
    turbidity = st.text_input("Turbidity", placeholder="Type Here")

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

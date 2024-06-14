import numpy as np
import pandas as pd
import joblib
import streamlit as st 
from PIL import Image

model = joblib.load('classifier.joblib')

image = Image.open('water.jpg')
st.image(image.resize((1000, 300)))

def predict_water_potability(ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity):
    prediction = model.predict([[ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity]])
    return prediction

def main():
    st.title("Water Potability Web APP")
    ph = st.text_input("ph", placeholder="Type Here") 
    Hardness = st.text_input("Hardness", placeholder="Type Here")
    Solids = st.text_input("Solids", placeholder="Type Here")
    Chloramines		= st.text_input("Chloramines", placeholder="Type Here")
    Sulfate			= st.text_input("Sulfate", placeholder="Type Here")
    Conductivity	= st.text_input("Conductivity", placeholder="Type Here")	
    Organic_carbon	= st.text_input("Organic_carbon", placeholder="Type Here")	
    Trihalomethanes	= st.text_input("Trihalomethanes", placeholder="Type Here")	
    Turbidity		= st.text_input("Turbidity", placeholder="Type Here")

    if st.button("Get Prediction"):
        output = predict_water_potability(ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity)
        st.session_state['prediction'] = output

    if 'prediction' in st.session_state:
        if st.session_state['prediction'] == 0:
            st.markdown("<h3>Result :<span style='color:red'> 0 </span></h3>", unsafe_allow_html=True)
        else:
            st.markdown("<h3>Result :<span style='color:LawnGreen'> 1 </span></h3>", unsafe_allow_html=True)
            
        st.markdown("<h5 style='color:red'> 0<span style='color:white'> =</span> Water is Not Potable (i.e. not safe for human consumption)</h5>", unsafe_allow_html=True)
        st.markdown("<h5 style='color:Blue'> 1<span  style='color:White'> =</span> Water is Potable (i.e. safe for human consumption)</h5>", unsafe_allow_html=True)
        
    if st.button("About"):
        st.text("Classifier name : Random Forest")
        st.text("Accuracy Score : 70.00")

if __name__ == '__main__':
    main()

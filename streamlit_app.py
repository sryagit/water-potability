import numpy as np
import pandas as pd
# import joblib
import streamlit as st 
from PIL import Image

# model = joblib.load('classifier.joblib')

image = Image.open('water.jpg')
st.image(image.resize((1000, 300)))

def predict_water_potability(ph, hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity):
    prediction = model.predict([[ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity]])
    return prediction

def main():
    #st.title("Banknote Authentication Classifier")
    st.title("Water Potability Web APP")
    ph			    = st.text_input("ph", placeholder="Type Here") 
    Hardness		= st.text_input("Hardness", placeholder="Type Here")
    Solids			= st.text_input("Solids", placeholder="Type Here")
    Chloramines		= st.text_input("Chloramines", placeholder="Type Here")
    Sulfate			= st.text_input("Sulfate", placeholder="Type Here")
    Conductivity	= st.text_input("Conductivity", placeholder="Type Here")	
    Organic_carbon	= st.text_input("Organic_carbon", placeholder="Type Here")	
    Trihalomethanes	= st.text_input("Trihalomethanes", placeholder="Type Here")	
    Turbidity		= st.text_input("Turbidity", placeholder="Type Here")

    if st.button("Get Prediction"):
        output = predict_water_potability(ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity)
        st.success(f'Result: {output}.')
        st.write('0 = Water is not Potable (water is not safe for human consumption)')
        st.write('1 = Water is Potable (water is safe for human consumption)')

    if st.button("About"):
        st.text("Classifier name : Random Forest")
        st.text("Accuracy Score : 70.00")

if __name__ == '__main__':
    main()

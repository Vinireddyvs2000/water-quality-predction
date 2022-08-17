import numpy as np
import pickle
import pandas as pd
import streamlit as st 

from PIL import Image

pickle_in= open("modeldep.pkl","rb")
df=pickle.load(pickle_in) 
    


def prediction(ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity):
    
    prediction=df.predict([[ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity]])
    print(prediction)
    return prediction

def main():
    st.title("Water Quality Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Water quality prediction </h2>
    </div>
    """
    
    
    st.markdown(html_temp,unsafe_allow_html=True)
    
    ph = st.number_input("ph",min_value=0.00,max_value=14.00)
    Hardness = st.number_input("Hardness", min_value=47.00,max_value=325.00)
    Solids = st.number_input("Solids", min_value=320.00,max_value=61230.00)
    Chloramines = st.number_input("Chloramines", min_value=0.30,max_value=13.20)
    Sulfate = st.number_input("Sulfate", min_value=129.00,max_value=480.00)
    Conductivity = st.number_input("Conductivity", min_value=181.00, max_value=755.00)
    Organic_carbon = st.number_input("Organic_carbon",min_value=2.00,max_value=30.00)
    Trihalomethanes = st.number_input("Trihalomethanes",min_value=0.00,max_value=124.00)
    Turbidity = st.number_input("Turbidity", min_value=1.00,max_value=7.00)
    result=""
  
       
    if st.button("Predict"):
        result = prediction(ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity)
  
    
    if (result==0):
        st.write("Not Potability")
    else:
        st.write("Potability")
    
    st.success('The output is {}'.format(result))
  
    
if __name__=='__main__':
    main()
    
    
    
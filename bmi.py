import streamlit as st
import pandas as pd

st.title("Welcome to BMI Calculator")

weight = st.number_input('Enter your weight in kilograms:', min_value=0.0, format="%.2f")
status = st.radio('Select your height format :', ('cms','meters','feet'))

try:
    if status == 'cms':
        height = st.number_input('Centimeters')
        bmi= weight/((height/100)**2)

    elif status == 'meters':
        height = st.number_input('meters')
        bmi= weight/((height)**2)

    else:
        height = st.number_input('feet')
        bmi= weight/((height/3.28)**2)
except:
    print('Zero division error')

if(st.button('Calculate BMI')):
    st.write('Your BMI index is {}'.format(round(bmi)))

    if bmi<16:
        st.error('You are extremely Underweight')
    elif(bmi>=16 and bmi<=18):
        st.warning('You are Underweight')
    elif(bmi>18 and bmi<=25):
        st.success('You are Healthy')
    elif(bmi>25 and bmi<=30):
        st.warning('You are Overweight')
    else:
        st.error('Your extremely Overweight')
import os
import pickle
import streamlit as st
import numpy as np
import pandas as pd



st.set_page_config(page_title="House Price Predictor",
                   layout="wide",
                   page_icon="🏠")

model = pickle.load(open('model_house.sav', 'rb'))

# page title
st.title('House Price Prediction Using ML')

# getting the input data from the user
col1, col2, col3 = st.columns(3)

with col1:

  SquareFootage = st.text_input('Square Footage')
  
  if SquareFootage: 
    
    try:
      SquareFootage = float(SquareFootage)
    except ValueError:
      # raise ValueError("SquareFootage field must be a valid number")
      st.error("Invalid Input")

with col2:
  
  Bathrooms = st.text_input('No of Bathrooms')
  
  if Bathrooms: 
    
    try:
      Bathrooms = float(Bathrooms)
    except ValueError:
      # raise ValueError("Bathrooms field must be a valid number")
      st.error("Invalid Input")
    
with col3:
  
  Bedrooms = st.text_input('No of Bedrooms')
  
  if Bedrooms: 
    
    try:
      Bedrooms = float(Bedrooms)
    except ValueError:
      # raise ValueError("Bedrooms field must be a valid number")
      st.error("Invalid Input")



# code for Prediction
diab_diagnosis = ''



def predict(input_data):
  input_data_as_numpy_array = np.asarray(input_data)
  # input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

  prediction = model.predict(input_data)
  return prediction




if st.button('Predict The Price'):

  
  user_input = [SquareFootage, Bathrooms, Bedrooms]

  
  # prediction = prediction(pd.DataFrame(user_input, columns=["SquareFootage","Bathrooms","Bedrooms"]))
  prediction = predict([user_input])

  st.success(prediction)
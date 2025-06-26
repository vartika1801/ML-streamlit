import streamlit as st
import pandas as pd
import numpy as np

st.title('Machine Learning App')

st.info('This is an app for Machine learning model')

with expander('Data'):
  st.write('**Raw Data**')
  df=pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df
  st.write('**X**')
  X=df.drop('species',axis=1)
  X
  st.write('**y**')
  y=df['species']
  y


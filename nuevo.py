import streamlit as st
import pandas as pd
import numpy as np



df_otorgada = pd.read_csv('https://raw.githubusercontent.com/JennyferRMcda/nueva/main/copia.csv')
@st.cache
def otorgada_data():
    df_otorgada = pd.read_csv('copia.csv')
    df_otorgada = df_otorgada.rename(columns={'latitud':'lat',
                                              'longitud':'lon',
                                              })     
    return df_otorgada
data = otorgada_data()
st.map(data)

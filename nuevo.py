import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame( np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(df)
archivo_excel = "coordenadas_de_centros_vac.xlsx"
hoja_excel = "coordenadas"
df = pd.read_excel(archivo_excel,
                   sheet_name = hoja_excel,
                   usecols = "A:C", )
st.dataframe(df)

df = df.rename(columns = {"latitud":"lat",
                          "longitud":"lon", })    

st.map(df)

df_otorgada = pd.read_csv("https://raw.githubusercontent.com/JennyferRMcda/nueva/main/coordenadas_de_centros_vac.csv")
@st.cache
def otorgada_data():
    df_otorgada = pd.read_csv('coordenadas_de_centros_vac.csv')
    df_otorgada = df_otorgada.rename(columns={
        'latitud':'lat',         
        'longitud':'lon',
    })
    return df_otorgada
data = otorgada_data()
st.map(data)

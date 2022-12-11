import streamlit as st
import pandas as pd
import numpy as np



#Importar el mapa de localización de los centros de vacunación
archivo_excel = "datonuevo.xlsx"
hoja_excel = "Centros de vacunacion final"
df = pd.read_excel(archivo_excel,
                   sheet_name = hoja_excel,
                   usecols = "A:C", )
st.dataframe(df)

@st.cache
def cvac():
    df_cvac = pd.read_excel(archivo_excel,
                            sheet_name = hoja_excel,
                            usecols = "A:C")
    df_cvac = df_cvac.rename(columns = {"latitud":"lat",
                                        "longitud":"lon",
                                       })                                 
    return df_cvac

st.map(cvac())

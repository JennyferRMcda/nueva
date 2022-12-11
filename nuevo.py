import streamlit as st
import pandas as pd
import numpy as np



#Importar el mapa de localización de los centros de vacunación
archivo_excel = "ultimamod.xlsx"
hoja_excel = "coordenadas"
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

import streamlit as st
import pandas as pd
archivo_excel = "DATOSF.xlsx"
hoja_excel = "TABLA1"
df = pd.read_excel(archivo_excel, 
                   sheet_name = hoja_excel,
                   usecols = "A:C")
st.dataframe(df)

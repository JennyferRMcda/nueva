import streamlit as st
import pandas as pd
archivo_excel = "coordenadas_de_centros_vac.xlsx"
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

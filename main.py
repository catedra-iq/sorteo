import pandas as pd
import streamlit as st
import numpy as np

N = 20
st.title(f"Sorteo de los {N} alumnes que pasarán a la comisión 6")


df = pd.read_csv('sorteo.csv', header= None)
df.columns = ["n","alumne", "cond" ]



if st.button("Sortear"):
    st.write(df.sample(n= N))




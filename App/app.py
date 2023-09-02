import streamlit as st
import pandas as pd
import numpy as np

st.title("Soccer Back")

st.sidebar.header("Season")
selected_season = st.sidebar.selectbox('Season', ['2022/2023','2021/2022','2020/2021'])

# Webscraping football data

def load-data(season):
    url = "https://www.football-data.co.uk/mmz4281/2324/"+season+".xlsx"
    data = pd.read_xlsx(url)
    return data

df = load_data(selected_season)


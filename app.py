import streamlit as st
import pandas as pd
import nunpy as sp
import http.client

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "XxXxXxXxXxXxXxXxXxXxXxXx"
    }

conn.request("GET", "/{endpoint}", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))







st.title("SoccerPrev")

st.sidebar.header("Leagues")

st.sidebar.header("Season")




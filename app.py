import streamlit as st
import pandas as pd
import plotly_express as px

data_VH = pd.read_csv("vehicles_us.csv")
hist_button = st.button('build histogram')
st.header('graphs about details of cars sales')

if hist_button:
    st.write('build a new histogram for data \
             related to the advertising \
                 of vehicles sales')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)


checkbox = st.checkbox('build graph')
st.header('Build a dispersion graph')

if checkbox:
    st.write('Make a new graph displaying the price in milles')
    fig = px.scatter(data_VH, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

!pip install --upgrade pip  

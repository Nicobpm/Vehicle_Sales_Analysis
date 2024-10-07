import streamlit as st
import pandas as pd
import plotly_express as px

data_VH = pd.read_csv("vehicles_us.csv")

data_VH['model_year'] = data_VH['model_year'].fillna(0).astype(int)

st.header('You can select the range of years to analyze')
min_year = 1908
max_year = 2019

selected_year = st.slider('Select year'
                          min_value=min_year,
                          max_value=max_year,
                          value=max_year,
                          step=1)
if selected_year:
    st.write('Year selected:', selected_year)
    fig = px.histogram(data_VH, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

st.header('Build a dispersion graph')
Button = st.button('Click to build graph')


if Button:
    st.write('Make a new graph displaying the price in milles')
    fig = px.scatter(data_VH, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)


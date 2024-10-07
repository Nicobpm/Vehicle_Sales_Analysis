import streamlit as st
import pandas as pd
import plotly_express as px

data_VH = pd.read_csv("vehicles_us.csv")

data_VH['model_year'] = data_VH['model_year'].fillna(0).astype(int)

st.header('We can see data about vehicles sales')
st.write("Please select the year of the car model to analize"
         )
min_year = 1908
max_year = 2019

selected_year = st.slider('Select year:',
                          min_value=min_year,
                          max_value=max_year,
                          value=max_year,
                          step=1)
filtered_year = data_VH[(data_VH['year'] >= selected_year[0]) & (
    data_VH['year'] <= selected_year[1])]

if not filtered_year.empty:
    st.write('Range of years to show:', selected_year)
    fig = px.scatter(filtered_year, x="odometer", y="price",
                     title=f'Scatter plot of Price vs Odometer \ 
                     for years {selected_year[0]} to {selected_year[1]}')
                     
    st.plotly_chart(fig, use_container_width=True)
else:
    st.write('No data available for the selected year range.')

st.header('Build a histogram for media odometer')
Button = st.button('Click to build graph')

if Button:
    st.write('Make a new graph displaying the price in milles')
    fig = px.histogram(data_VH, x="odometer")
    st.plotly_chart(fig, use_container_width=True)


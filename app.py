import streamlit as st
import pandas as pd
import plotly_express as px
# Read the file
data_VH = pd.read_csv("vehicles_us.csv")
# Fill in the empty model_years and convert to Number column
data_VH['model_year'] = data_VH['model_year'].fillna(0).astype(int)

# Create a header about the process
st.header('We can see data about vehicles sales')
st.write("Please select the year of the car model to analize"
         )
min_year = 1908
max_year = 2019

# Make a slider to control for customers between model years
selected_year = st.slider('Select year range:',
                          min_value=min_year,
                          max_value=max_year,
                          value=(min_year, max_year),
                          step=1)
filtered_year = data_VH[(data_VH['model_year'] >= selected_year[0]) &
                        (data_VH['model_year'] <= selected_year[1])]

# Crate a scatter using the filter by slider
if not filtered_year.empty:
    st.write('Range of years to show:', selected_year)
    title = f'scatter graph of Price vs miles for years {selected_year[0]} to {selected_year[1]}'
    fig = px.scatter(
        filtered_year,
        x="odometer",
        y="price",
        title=title
    )

    st.plotly_chart(fig, use_container_width=True)
else:
    st.write('No data available for the selected year range.')

# Create a graph using button for histogram
st.header('Build a histogram for media odometer')
Button = st.button('Click to build graph')

if Button:
    st.write('displaying histogram in milles')
    fig = px.histogram(data_VH, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

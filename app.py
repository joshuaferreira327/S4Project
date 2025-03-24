import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('vehicles_us.csv')
    return df

df = load_data()

# Fill missing values and drop duplicates
df['model_year'] = df['model_year'].fillna(df['model_year'].median())
df['cylinders'] = df.groupby('model')['cylinders'].transform(lambda x: x.fillna(x.median()))
df['odometer'] = df.groupby('model')['odometer'].transform(lambda x: x.fillna(x.median()))
df['paint_color'] = df['paint_color'].fillna('Unknown')
df = df.drop_duplicates()

# Title and header
st.title("🚗 Car Listings Dashboard")
st.header("Explore Car Price Trends and Mileage")

# Checkbox to filter out entries with price = 0
if st.checkbox("Exclude listings with price = 0"):
    df = df[df['price'] > 0]

# Histogram of car prices
st.subheader("Histogram of Car Prices")
fig_price = px.histogram(df, x='price', nbins=50, title='Distribution of Car Prices')
st.plotly_chart(fig_price)

# Scatter plot of price vs. model year
st.subheader("Price vs. Model Year")
fig_year_price = px.scatter(
    df, x='model_year', y='price',
    color='condition',
    title='Car Price vs. Model Year by Condition'
)
st.plotly_chart(fig_year_price)

# Scatter plot of price vs. odometer
st.subheader("Price vs. Odometer Reading")
fig_odometer_price = px.scatter(
    df, x='odometer', y='price',
    color='fuel',
    title='Car Price vs. Odometer by Fuel Type'
)
st.plotly_chart(fig_odometer_price)

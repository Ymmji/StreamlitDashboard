import streamlit as st
import pandas as pd


st.title('Tree Census')
data = pd.read_csv('tree_census_new.csv')
st.write(data)

st.bar_chart(data['tree_dbh'][0:1000])
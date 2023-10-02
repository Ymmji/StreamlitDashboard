import streamlit as st
import pandas as pd
import yfinance as yf

user_input = st.text_input("Enter stock name", 'TSLA')

st.write(user_input)

st.title(user_input)
#ticker= yf.Ticker('TSLA')
ticker= yf.Ticker(user_input)
data = ticker.history(period = '5Y')
st.write(data)




st.line_chart(data['Close'])

#make a drop down menu
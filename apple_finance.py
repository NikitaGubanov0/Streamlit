import streamlit as st
import pandas as pd
import yfinance as yf

st.title("""
         Данные о котировках компании Apple
         """)


tickerSymbol = 'AAPL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2014-10-10', end='2024-10-10')

st.write("""
         ### Анализ котировок
         """)
st.line_chart(tickerDf.Open)

st.write("""
         ### Выплата дивидендов
         """)
st.line_chart(tickerDf.Dividends)

st.write("""
         ### Объем торгов за год
         """)
st.line_chart(tickerDf.Volume)


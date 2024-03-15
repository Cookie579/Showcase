import streamlit as st
from datetime import date
import yfinance as yf
# from prophet import Prophet
# from prophet.plot import plot_plotly

from plotly import graph_objs as go
import time

import Display
from Display import *


def search():
    stocks = []

    f = open("all_tickers.txt", "r")
    for x in f:
        stocks.append(x)

    selected_stock = st.selectbox('Select stock', stocks, key='S')

    display(selected_stock)
    return selected_stock


def p_search():
    stocks = []

    f = open("all_tickers.txt", "r")
    for x in f:
        stocks.append(x)

    selected_stock_p = st.selectbox('Select stock', stocks, key='P')
    return selected_stock_p


import streamlit as st
from datetime import date
import yfinance as yf

from plotly import graph_objs as go
import time

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")
selected_stock = ''



@st.cache_data
def load_data(ticker):
    global data
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data


def display(ticker):
    global data
    ma_20 = []
    ma_50 = []
    ma_120 = []

    with st.spinner(text='In progress'):

        time.sleep(1)
        data = yf.download(ticker, START, TODAY)
        data.reset_index(inplace=True)

        # ... TEST
        ma_df = load_data(ticker)
        ma_df['20_SMA'] = ma_df['Close'].rolling(window=20, min_periods=1).mean()
        ma_df['50_SMA'] = ma_df['Close'].rolling(window=50, min_periods=1).mean()
        ma_df['120_SMA'] = ma_df['Close'].rolling(window=240, min_periods=1).mean()

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))

        for n in ma_df['20_SMA']:
            ma_20.append(n)

        for n in ma_df['50_SMA']:
            ma_50.append(n)

        for n in ma_df['120_SMA']:
            ma_120.append(n)

        fig.add_trace(go.Scatter(x=data['Date'], y=ma_20, name="20 Day MA", visible='legendonly'))
        fig.add_trace(go.Scatter(x=data['Date'], y=ma_50, name="50 Day MA", visible='legendonly'))
        fig.add_trace(go.Scatter(x=data['Date'], y=ma_120, name="120 Day MA"))

        fig.layout.update(title_text=f'{ticker}| Price Chart', xaxis_rangeslider_visible=True)
        st.plotly_chart(fig)

        st.success('Done')

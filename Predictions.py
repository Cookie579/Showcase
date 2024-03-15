import streamlit as st
from datetime import date
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly

from plotly import graph_objs as go
import time

import Display
import Search
from Display import *
from Search import *


def predict():
    n_months = st.slider('Months of prediction:', 1, 36)
    period = n_months * 30

    data = Display.load_data(Search.p_search())

    df_train = data[['Date', 'Close']]
    df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

    m = Prophet()
    m.fit(df_train)
    future = m.make_future_dataframe(periods=period)
    forecast = m.predict(future)

    if n_months == 1:
        st.write(f'Forecast plot for {n_months} month')

    else:
        st.write(f'Forecast plot for {n_months} months')

    fig1 = plot_plotly(m, forecast)
    st.plotly_chart(fig1)

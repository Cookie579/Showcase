import streamlit as st
from datetime import date
import yfinance as yf
# from prophet import Prophet
# from prophet.plot import plot_plotly
from plotly import graph_objs as go
import time

import Search
from Search import *

import Predictions
from Predictions import *


with st.sidebar:
    # Center-aligned headers
    st.markdown("<h1 style='text-align: left;'>Inbox</h1>", unsafe_allow_html=True)
    # st.markdown("<p style='text-align: center;'><button>Button 1</button></p>", unsafe_allow_html=True)

    # st.markdown("<h1 style='text-align: center;'>Sidebar Header 2</h1>", unsafe_allow_html=True)

    # Center-aligned buttons
    # st.markdown("<p style='text-align: center;'><button>Button 2</button></p>", unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["Nov 29, \'23", "June 17, \'23"])
    tab1.write(f"""this is tab 1""")
    tab2.write(f"""this is tab 2""")


st.title('Agasthya\'s Stock Picks')

tab1, tab2, tab3 = st.tabs(["Search", "Predictions", "Portfolio"])
tab1.write("Search Stocks")
tab2.write("Predictions based on AI")

# Search
with tab1:
    Search.search()

# Predictive
with tab2:
    Predictions.predict()

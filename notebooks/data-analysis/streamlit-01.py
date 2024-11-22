import streamlit as st
import pandas as pd
import os
import plotly.graph_objects as go

# Streamlit configs
st.set_page_config(page_title="Portfolio Risk Management", layout="wide")

# Import Data
script_dir = os.path.dirname(os.path.abspath(__file__))
btc_file = 'btcusd_daily_agg_real.csv'
sol_file = 'solusd_daily_agg_real.csv'
btc_file_path = os.path.join(script_dir, "../../data/" + btc_file)
sol_file_path = os.path.join(script_dir, "../../data/" + sol_file)
btc_df = pd.read_csv(btc_file_path)
sol_df = pd.read_csv(sol_file_path)

st.markdown("# Portfolio Risk Management")

fig = go.Figure()
fig.add_trace(go.Candlestick(x=btc_df['timestamp'],
                        open=btc_df['open'],
                        high=btc_df['high'],
                        low=btc_df['low'],
                        close=btc_df['close'])
)

fig.update_layout(
    title={
        'text': "BTCUSD Daily Aggregated Real Data", 
        'font': {'size': 32},
        'x':0.5,
        'xanchor': 'center'
        },
    xaxis_title="Date",
    yaxis_title="Price",
    height=800
    )
st.plotly_chart(fig)

fig = go.Figure(
    data=[go.Candlestick(x=sol_df['timestamp'],
                            open=sol_df['open'],
                            high=sol_df['high'],
                            low=sol_df['low'],
                            close=sol_df['close'])]
)
# add title
fig.update_layout(
    title={
        'text': "SOLUSD Daily Aggregated Real Data", 
        'font': {'size': 32},
        'x':0.5,
        'xanchor': 'center'
        },
    xaxis_title="Date",
    yaxis_title="Price",
    height=800
    )
st.plotly_chart(fig)
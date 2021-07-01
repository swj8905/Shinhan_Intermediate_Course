import yfinance as yf
import streamlit as st
import datetime
import plotly.graph_objects as go

# st.write("# 주식 데이터 시각화")
"# 주식 데이터 시각화"

ticker = st.text_input("티커 입력")
data = yf.Ticker(ticker)
today = datetime.datetime.today().strftime("%Y-%m-%d")
df = data.history(period="1d",
             start="2015-1-1",
             end=today)
st.dataframe(df)

"## 주가 차트 - 종가 기준"
st.line_chart(df["Close"])

"## 주가 차트 - 캔들 차트"
layout = go.Layout()
data = go.Candlestick(x=df.index,
        open=df["Open"], close=df["Close"],
        low=df["Low"], high=df["High"])
fig = go.Figure(data=[data], layout=layout)
st.plotly_chart(fig)

"## 거래량"
st.bar_chart(df["Volume"])
import streamlit as st
import pandas as pd 
import numpy as np
import requests,os,calendar,csv,sys
from datetime import date
from dotenv import load_dotenv

sys.path.append("Ethereum Historical Data copy.csv")
load_dotenv()
finance_key = os.getenv("new_finance_api_key")


# url = "https://yahoo-finance127.p.rapidapi.com/price/eth-usd"

# headers = {
# 	"x-rapidapi-key": finance_key,
# 	"x-rapidapi-host": "yahoo-finance127.p.rapidapi.com",
# 	"Content-Type": "application/json"
# }

# response = requests.get(url, headers=headers)

# record_data = response.json()


month = date.today().strftime("%m")
dated = date.today().strftime("%d")
year = date.today().strftime("%Y")
current_month = calendar.month_name[int(month)]

date_today = current_month+" "+dated+", "+year
data = {
    "Date": date_today,
    "Price": "1234",
    "Open": "2234",
    "High": "4221",
    "Low": "2123",
    "Vol": "234k",
    "Change %": "-1.0%"
}

# price = record_data['regularMarketPrice']['fmt']
# open_price = record_data['regularMarketOpen']['fmt']
# high = record_data['regularMarketDayHigh']['fmt']
# low = record_data['regularMarketDayLow']['fmt']
# vol = record_data['regularMarketVolume']['fmt']
# change_in_percent = record_data['regularMarketChangePercent']['fmt']

# ----------------------------
# st.write(f"Date Today: {date_today}")
# st.write(f"Price Today: {price}")
# st.write(f"Open Price Today: {open_price}")
# st.write(f"24h High Today: {high}")
# st.write(f"24h Low Today: {low}")
# st.write(f"Vol Today: {vol}")
# st.write(f"Change in %: {change_in_percent}")

# ----------------------------
st.write("Stock Market Data")
st.write(data)


# ----------------------------
with open("Ethereum Historical Data copy.csv","r") as f:
    st.write(f.read())
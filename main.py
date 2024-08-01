import requests
from config import *
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


class TradingClass:
    def __init__(self):
        
        # Initialize headers for GET and POST requests with Alpaca API credentials
        self.get_header = {
                "accept":"application/json",
                "APCA-API-KEY-ID":API_KEY,
                "APCA-API-SECRET-KEY":SECRET_KEY
                }
        self.post_header = {
                "accept":"application/json",
                "content-type":"application/json",
                "APCA-API-KEY-ID":API_KEY,
                "APCA-API-SECRET-KEY":SECRET_KEY
                }
        
        # Initialize dictionaries to store stock data
        self.top_active_stocks = {}
        self.top_market_movers_gainers = {}
        self.top_market_movers_losers = {}

    # Fetch and display the top 10 most active stocks by volume
    def scan_for_most_active_stocks(self):
        url = "https://data.alpaca.markets/v1beta1/screener/stocks/most-actives?by=volume&top=10"
        response = requests.get(url, headers=self.get_header)
        response_data = response.json()

        # Store and print the top active stocks
        self.top_active_stocks = response_data["most_actives"]
        print(f"\n Printing the value of self.top_stocks_by_volume\n {self.top_active_stocks} ")

        # Convert the data to a DataFrame and sort by volume
        df = pd.DataFrame(self.top_active_stocks)
        volume_ascending = df[["symbol","volume"]].sort_values(by="volume", ascending=True)
        print(volume_ascending)
 
        # Use Streamlit to display the data
        st.title("Top 10 stocks by Volume")
        st.bar_chart(df, x="symbol", y="trade_count", color=("#fefae0"))
        st.bar_chart(df, x='symbol', y='volume', color=("#dda15e"))
    
    
    # Fetch and display the top 10 market movers (gainers and losers)
    def scan_for_top_market_mover_stocks(self):
        url = "https://data.alpaca.markets/v1beta1/screener/stocks/movers?top=10"
        
        response = requests.get(url, headers=self.get_header)
        print(f"The response code is {response.status_code}")
        response_data = response.json()
        print(response_data)
        #self.top_market_movers_stock = response_data
        #print(response_data.keys()) 
        
        # Store and print the top market movers
        self.top_market_movers_gainers = response_data['gainers']
        self.top_market_movers_losers = response_data['losers']         
        
        # Convert the data to DataFrames
        df_gainers = pd.DataFrame(self.top_market_movers_gainers)
        df_losers = pd.DataFrame(self.top_market_movers_losers) 

        # Use Streamlit to display the top gainers and losers
        st.text("These are the top gainers")
        st.table(df_gainers)
        st.text("These are the top losers")
        st.table(df_losers)   

# run the data scanning methods
trading_obj = TradingClass()
trading_obj.scan_for_most_active_stocks()
trading_obj.scan_for_top_market_mover_stocks()        

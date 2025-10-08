# Stock Portfolio Tracker
# Tracks your stock portfolio using live data from Yahoo Finance

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import argparse

# function to download the latest stock prices
def fetch_prices(tickers):
    # get the most recent "Close" price for each ticker
    data = yf.download(tickers, period="1d", interval="1m")['Close'].iloc[-1]
    return data

# function to display portfolio info + plot pie chart
def show_portfolio(data, shares):
    # build a small dataframe to store calculations
    df = pd.DataFrame({
        'Ticker': data.index,
        'Shares': [shares[t] for t in data.index],
        'Price': data.values
    })

    # calculate total value for each stock
    df['Value'] = df['Shares'] * df['Price']
    df['% of Portfolio'] = df['Value'] / df['Value'].sum() * 100

    # print everything nicely
    print("\nYour Portfolio:\n")
    print(df[['Ticker', 'Price', 'Shares', 'Value', '% of Portfolio']])
    print(f"\nTotal Portfolio Value: ${df['Value'].sum():.2f}")

    # plot pie chart
    plt.figure(figsize=(6, 6))
    plt.pie(df['Value'], labels=df['Ticker'], autopct='%1.1f%%')
    plt.title("Portfolio Allocation")
    plt.show()

if __name__ == "__main__":
    # let the user pass in tickers and shares from the command line
    parser = argparse.ArgumentParser(description="Simple Stock Portfolio Tracker")
    parser.add_argument('--tickers', nargs='+', default=["AAPL", "MSFT", "NVDA", "TSLA"],
                        help="List of stock tickers (space separated)")
    parser.add_argument('--shares', nargs='+', type=int, default=[10, 5, 3, 2],
                        help="Number of shares for each ticker (space separated)")
    args = parser.parse_args()

    # zip tickers + shares together into a dictionary
    tickers = args.tickers
    shares = dict(zip(tickers, args.shares))

    # get data + show results
    prices = fetch_prices(tickers)
    show_portfolio(prices, shares)

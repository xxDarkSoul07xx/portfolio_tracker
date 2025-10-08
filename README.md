This is a simple Python tool that will track and visualize your stock portfolio using real-time data. It is built using pandas, matplotlib, and yfinance.

## Features
1. Fetches live stock prices automatically
2. Calculates the total value and percentage allocation per stock
3. Displays a clean and easy to read pie chart of your portfolio composition

This uses the MIT License - feel free to use it, just give credit

## To run
```bash
pip install -r requirements.txt
python portfolio_tracker.py --tickers AAPL MSFT NVDA TSLA --shares 10 5 3 2

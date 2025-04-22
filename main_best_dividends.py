import yfinance as yf
import time
import json
# from math import pi

from lib.yahoofinance import get_stock_info, get_stock_price, get_stock_dividend, get_biggest_dividend
from lib.ticker_fetcher import get_all_tickers

def main():
    all_tickers = get_all_tickers()
    print(all_tickers)
    print(get_biggest_dividend(all_tickers))

if __name__ == "__main__":
    main()
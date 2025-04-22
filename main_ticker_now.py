import yfinance as yf
import time
import json
# from math import pi

from lib.yahoofinance import get_stock_info, get_stock_price, get_stock_dividend

def main():
    ticker = "NVDA"  # Replace with your desired stock ticker
    previous_price = 0
    price_change = 0
    while True:
        stock_info = get_stock_info(ticker)
        price = get_stock_price(stock_info)
        market_state_str = ''
        # print(stock_info['marketState'])
        market_state = stock_info['marketState']
        # REGULAR, PRE
        # if (stock_info['marketState'] == 'PRE' or stock_info['marketState'] == 'POST'):
        #     market_state_str = f"{stock_info['marketState']}: {stock_info['preMarketChange']}"
        # else:
        #     market_state_str = f"{stock_info['marketState']}: {stock_info['regularMarketChange']}"
        match market_state:
            case 'PRE':
                market_state_str = f"{stock_info['marketState']}: {stock_info['preMarketChange']}"
            case 'POST':
                market_state_str = f"{stock_info['marketState']}: {stock_info['postMarketChange']}"
            case 'REGULAR':
                market_state_str = f"{stock_info['marketState']}: {stock_info['regularMarketChange']}"
            # If an exact match is not confirmed, this last case will be used if provided
            case _:
                return "Something's wrong with the internet"
        if (previous_price != 0):
            price_change = price - previous_price
        # print(f"Current price of {ticker} ({market_state}, {stock_info['quickRatio']}, {stock_info['currentRatio']}, {0}, {0:.2f}): {price} ".format(price_change,(price_change / price)*100))
        print(f"Current price of {ticker} ({market_state_str}, {stock_info['quickRatio']}, {stock_info['currentRatio']}, {price_change:.5f}, {(price_change / price)*100:.2f}%): {price} ")
        previous_price = price
        time.sleep(5)  # Wait 5 seconds before polling again

if __name__ == "__main__":
    main()
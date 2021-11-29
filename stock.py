import yfinance as yf

def get_info(s):
    return yf.Ticker(s)
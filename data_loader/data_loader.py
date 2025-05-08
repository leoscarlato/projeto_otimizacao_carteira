import pandas as pd

def load_prices(file):
    df = pd.read_csv(file, index_col=0, parse_dates=True)
    return df

def calculate_daily_returns(prices):
    return prices.pct_change().dropna()
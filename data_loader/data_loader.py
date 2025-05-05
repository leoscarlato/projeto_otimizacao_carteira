import yfinance
import pandas as pd

acoes = [
    "UNH", "GS", "MSFT", "HD", "V", "SHW", "MCD", "CAT", "AMGN", "AXP",
    "TRV", "CRM", "IBM", "JPM", "AAPL", "HON", "AMZN", "PG", "BA", "JNJ",
    "CVX", "MMM", "NVDA", "WMT", "DIS", "MRK", "KO", "CSCO", "NKE", "VZ"
]

data = yfinance.download(acoes, start="2024-08-01", end="2024-12-31")
data_final = data['Close']
data_final.to_csv('data_loader/acoes.csv')

def load_prices(file):
    df = pd.read_csv(file, index_col=0, parse_dates=True)
    return df

def calculate_daily_returns(prices):
    return prices.pct_change().dropna()
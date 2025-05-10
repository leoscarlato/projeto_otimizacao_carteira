import pandas as pd

def load_prices(file):
    """
    Carregamento dos dados de preços a partir de um arquivo CSV.
    """
    df = pd.read_csv(file, index_col=0, parse_dates=True)
    return df

def calculate_daily_returns(prices):
    """
    Cálculo dos retornos diários a partir dos preços.
    Os retornos diários são calculados como a variação percentual dos preços em relação ao dia anterior.
    """
    return prices.pct_change().dropna()
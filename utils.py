import numpy as np

def mean(x):
    return np.mean(x)

def stddev(x):
    return np.std(x, ddof=1)

def covariance_matrix(returns):
    return np.cov(returns.T)

def sharpe_ratio(portfolio_return, risk_free, portfolio_vol):
    return (portfolio_return - risk_free) / portfolio_vol
import numpy as np

def mean(x):
    return np.mean(x)

def stddev(x):
    return np.std(x, ddof=1)

def covariance_matrix(returns):
    return np.cov(returns.T)

def sharpe_ratio(portfolio_return, risk_free, portfolio_vol):
    return (portfolio_return - risk_free) / portfolio_vol

def generate_random_weights(n):
    while True:
        w = np.random.rand(n)
        w /= w.sum()
        if np.all(w <= 0.2):
            return w

def calculate_portfolio_return(weights, mean_returns):
    return np.dot(weights, mean_returns) * 252

def calculate_portfolio_volatility(weights, cov_matrix):
    return np.sqrt(np.dot(weights.T, np.dot(cov_matrix * 252, weights)))
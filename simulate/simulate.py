import numpy as np
from utils import generate_random_weights, calculate_portfolio_return, calculate_portfolio_volatility
from utils import sharpe_ratio

def simulate_combination(assets, daily_returns):
    mean_returns = daily_returns[list(assets)].mean()
    cov_matrix = daily_returns[list(assets)].cov()
    best_sharpe = -np.inf
    best_result = {}

    for _ in range(1000):
        weights = generate_random_weights(25)
        port_return = calculate_portfolio_return(weights, mean_returns)
        port_vol = calculate_portfolio_volatility(weights, cov_matrix)
        sr = sharpe_ratio(port_return, 0.02, port_vol)

        if sr > best_sharpe:
            best_sharpe = sr
            sorted_assets = sorted(zip(assets, weights), key=lambda x: x[1], reverse=True)
            best_result = {'sharpe': sr, 'assets': sorted_assets}

    return best_result
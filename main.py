from data_loader.data_loader import load_prices, calculate_daily_returns
from simulate import generate_random_weights, calculate_portfolio_return, calculate_portfolio_volatility
from utils import sharpe_ratio
import itertools
import numpy as np
from tqdm import tqdm

prices = load_prices('data_loader/acoes.csv')
daily_returns = calculate_daily_returns(prices)

best_sharpe = -np.inf
best_result = {}

for assets in tqdm(itertools.combinations(prices.columns, 25)):
    selected_returns = daily_returns[list(assets)]
    mean_returns = selected_returns.mean()
    cov_matrix = selected_returns.cov()

    for _ in range(100):
        weights = generate_random_weights(25)
        port_return = calculate_portfolio_return(weights, mean_returns)
        port_vol = calculate_portfolio_volatility(weights, cov_matrix)
        sr = sharpe_ratio(port_return, 0.02, port_vol)

        if sr > best_sharpe:
            best_sharpe = sr
            sorted_assets = sorted(zip(assets, weights), key=lambda x: x[1], reverse=True)
            best_result = {
                'sharpe': sr,
                'assets': sorted_assets
            }

print(f"Best Sharpe Ratio: {best_result['sharpe']:.4f}")
print("Assets and Weights (sorted):")
for asset, weight in best_result['assets']:
    print(f"{asset}: {weight:.4f}")
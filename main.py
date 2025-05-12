import itertools
import numpy as np
from tqdm import tqdm
from concurrent.futures import ProcessPoolExecutor, as_completed
from data_loader.data_loader import load_prices, calculate_daily_returns
from simulate.simulate import simulate_combination

if __name__ == "__main__":
    prices = load_prices('data_loader/acoes.csv')
    daily_returns = calculate_daily_returns(prices)

    all_combinations = list(itertools.combinations(prices.columns, 25))
    overall_best_sharpe = -np.inf
    overall_best_result = {}

    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(simulate_combination, comb, daily_returns) for comb in all_combinations]
        
        for f in tqdm(as_completed(futures), total=len(futures)):
            result = f.result()
            if result['sharpe'] > overall_best_sharpe:
                overall_best_sharpe = result['sharpe']
                overall_best_result = result

    print(f"Best Sharpe Ratio: {overall_best_result['sharpe']:.4f}")
    print(f"Portfolio Volatility: {overall_best_result['volatility']:.4f}")
    print(f"Portfolio Return: {overall_best_result['return']:.4f}")
    print("Assets and Weights (sorted):")
    for asset, weight in overall_best_result['assets']:
        print(f"{asset}: {weight:.4f}")
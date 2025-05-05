import numpy as np
import utils

def generate_random_weights(n):
    weights = np.random.rand(n)
    return weights / np.sum(weights)

def calculate_portfolio_return(weights, mean_returns):
    return np.dot(weights, mean_returns) * 252

def calculate_portfolio_volatility(weights, cov_matrix):
    return np.sqrt(np.dot(weights.T, np.dot(cov_matrix * 252, weights)))
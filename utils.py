import numpy as np

def sharpe_ratio(portfolio_return, risk_free, portfolio_vol):
    """
    Calcula o Sharpe Ratio de um portfólio, isto é, a relação entre o retorno do portfólio e o risco assumido.
    """
    return (portfolio_return - risk_free) / portfolio_vol

def generate_random_weights(n):
    """
    Geração de pesos aleatórios para o portfólio.
    Os pesos gerados são normalizados de forma a seguir as restrições:
    - Cada peso deve ser menor ou igual a 0.2
    - A soma dos pesos deve ser igual a 1
    """
    while True:
        w = np.random.rand(n)
        w /= w.sum()
        if np.all(w <= 0.2):
            return w

def calculate_portfolio_return(weights, mean_returns):
    """
    Calcula o retorno esperado do portfólio, considerando os pesos e os retornos médios dos ativos.
    O retorno esperado é calculado como o produto dos pesos e dos retornos médios, multiplicado por 252 (número de dias úteis em um ano).
    Os retornos médios são multiplicados por 252 para anualizar o retorno.
    """
    return np.dot(weights, mean_returns) * 252

def calculate_portfolio_volatility(weights, cov_matrix):
    """
    Calcula a volatilidade do portfólio.
    A volatilidade é calculada como a raiz quadrada do produto dos pesos, da matriz de covariância e dos pesos transpostos.
    A matriz de covariância é multiplicada por 252 para anualizar a volatilidade.
    """
    return np.sqrt(np.dot(weights.T, np.dot(cov_matrix * 252, weights)))
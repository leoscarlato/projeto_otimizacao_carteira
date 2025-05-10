# Otimização de Carteira de Investimentos - 2º Semestre de 2024

## Descrição
Este projeto busca identificar a combinação ótima de 25 ativos dentre um universo de 30 do índice Dow Jones, com o objetivo de maximizar o Sharpe Ratio. A alocação de pesos é avaliada por meio de simulações puras, respeitando restrições de longo prazo (long-only) e peso máximo por ativo

## Objetivos
- Encontrar a combinação ótima de 25 ativos dentre um universo de 30.
- Maximizar o Sharpe Ratio.
- Utilizar diferentes simulações para atribuir pesos a cada ativo, garantindo que a soma desses seja igual a 1 e que nenhum ativo tenha peso negativo ou superior a 0,2.
- Avaliar o desempenho da carteira com o maior Sharpe Ratio.

## Metodologia
1. **Coleta de Dados**

    Foi utilizada a biblioteca `yfinance` para baixar preços diários ajustados dos 30 ativos do índice Dow Jones entre as datas 01/08/2024 e 31/12/2024.

    Os dados são salvos em `data_loader/acoes.csv`. Caso queira analizar o código responsável por essa coleta, este se encontra em `data_loader/data_fetcher.py`.

2. **Cálculo do Retorno Diário**

    No arquivo `data_loader/data_loader.py`, existem duas funções principais responsáveis por carregar os dados e calcular o retorno diário dos ativos:

    - `load_prices`: realiza a leitura do arquivo CSV contendo os preços ajustados dos ativos, e o transforma em um DataFrame, utilizando a biblioteca `pandas`.

    - `calculate_daily_returns`: calcula o retorno diário dos ativos, aplicando a função `pct_change` do `pandas` para calcular a variação percentual entre os preços ajustados de um dia para o outro, além da função `dropna` para remover os valores nulos resultantes do cálculo. O resultado é um DataFrame contendo os retornos percentuais diários dos ativos.

3. **Geração de Combinações de Ativos**

    Utilizando a biblioteca `itertools`, mais especificamente a função `combinations`, são geradas todas as combinações possíveis de 25 ativos dentre os 30 disponíveis, resultando em um total de **142506** combinações, as quais são armazenadas dentro de uma lista chamada `all_combinations`.

4. **Simulação de Carteiras**

    Para cada combinação de 25 ativos:
    - Calcula-se o vetor de retornos médios e a matriz de covariância anualizada (Σ_dia × 252).

    - Executam-se 1.000 iterações de geração de pesos via generate_random_weights(n), assegurando soma = 1 e peso ≤ 20%.

    - Para cada vetor de pesos:

        1. Calcula-se o retorno anual (função `calculate_portfolio_return`).
        2. Calcula-se a volatilidade anual (função `calculate_portfolio_volatility`).
        3. Computa-se o Sharpe Ratio (função `sharpe_ratio`).

    - Mantém-se apenas a simulação com maior Sharpe Ratio.

5. **Paralelização**

    Por se tratar de uma tarefa computacionalmente mais demandante, a execução do código pode levar um tempo considerável, especialmente ao lidar com um grande número de combinações e simulações. Assim, a fim de otimizar o tempo de execução, o código foi estruturado de forma a permitir a execução em paralelo, técnica que possibilita a execução simultânea de múltiplas tarefas, aproveitando melhor os recursos computacionais disponíveis. 
    
    Para isso, foi utilizada a biblioteca `concurrent.futures`, especificamente o módulo `ProcessPoolExecutor`, que permite a execução de funções em paralelo utilizando múltiplos processos.

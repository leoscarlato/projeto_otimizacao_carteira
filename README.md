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

6. **Resultado final**

    Ao fim, o script exibe o Sharpe Ratio máximo encontrado e a alocação dos 25 ativos correspondentes com seus respectivos pesos.

## Estrutura do Projeto
```
├── data_loader/
│   └── data_fetcher.py
│   └── data_loader.py
│   └── acoes.csv  
├── utils.py              
├── simulate/
│   └── simulate.py    
└── main.py               
```
- `data_loader/`: contém os scripts responsáveis pela coleta e processamento dos dados, além do arquivo CSV com os preços ajustados dos ativos.
- `utils.py`: contém funções auxiliares utilizadas em todo o projeto, como o cálculo do retorno, volatilidade, Sharpe Ratio, além da geração de pesos aleatórios.
- `simulate/`: contém o script responsável pela simulação de carteiras, incluindo a geração de combinações de ativos e a execução das simulações para verificar o desempenho de cada carteira.
- `main.py`: script principal que executa o fluxo do projeto, chamando as funções necessárias para a coleta de dados, processamento, simulação com paralelização e exibição dos resultados.

## Requisitos

Para rodar o programa, primeiramente é necessário ter o Python instalado em sua máquina, preferencialmente a versão 3.11.9 ou superior. Além disso, é necessário instalar algumas bibliotecas listadas como dependências no arquivo `requirements.txt`. Para isso, você pode utilizar o gerenciador de pacotes `pip` da seguinte forma:

```bash
pip install -r requirements.txt
```

## Execução
Para executar o programa, primeiramente é necessário obter os dados dos ativos. Para isso, após ter instalado todas as dependências, execute o seguinte comando em seu terminal:

```bash
python data_loader/data_fetcher.py
```

Com isso, o arquivo `acoes.csv` será gerado na pasta `data_loader/`, contendo os preços ajustados dos ativos do índice Dow Jones entre as datas 01/08/2024 e 31/12/2024.
Após esta etapa, você já pode executar o script principal do projeto, que irá realizar a simulação e exibir os resultados, por meio do seguinte comando:

```bash
python main.py
```


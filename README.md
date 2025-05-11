# Otimização de Carteira de Investimentos - 2º Semestre de 2024

## Descrição
Este projeto busca identificar a combinação ótima de 25 ativos dentre um universo de 30 do índice Dow Jones, com o objetivo de maximizar o Sharpe Ratio e, consequentemente, o retorno ajustado ao risco. A abordagem utilizada envolve a geração de combinações de ativos e a simulação de diferentes alocações de pesos, respeitando certas restrições.

## Objetivos
- Encontrar a combinação ótima de 25 ativos dentre um universo de 30.
- Maximizar o Sharpe Ratio.
- Utilizar diferentes simulações para atribuir pesos a cada ativo, garantindo que a soma desses seja igual a 1 e que nenhum ativo tenha peso negativo ou superior a 0,2.
- Avaliar o desempenho da carteira com o maior Sharpe Ratio.

## Estrutura do Projeto
```
├── data_loader/
│   └── data_fetcher.py
│   └── data_loader.py
├── utils.py              
├── simulate/
│   └── simulate.py    
├── main.py  
└── requirements.txt                  
```
- `data_loader/`: contém os scripts responsáveis pela coleta e processamento dos dados, além do arquivo CSV com os preços ajustados dos ativos.
- `utils.py`: contém funções auxiliares utilizadas em todo o projeto, como o cálculo do retorno, volatilidade, Sharpe Ratio, além da geração de pesos aleatórios.
- `simulate/`: contém o script responsável pela simulação de carteiras, incluindo a geração de combinações de ativos e a execução das simulações para verificar o desempenho de cada carteira.
- `main.py`: script principal que executa o fluxo do projeto, chamando as funções necessárias para a coleta de dados, processamento, simulação com paralelização e exibição dos resultados.
- `requirements.txt`: lista de dependências necessárias para o projeto.


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

    - Executam-se 1.000 iterações de geração de pesos via `generate_random_weights(n)`, assegurando soma = 1 e peso ≤ 20%.

    - Para cada vetor de pesos:

        1. Calcula-se o retorno anual (função `calculate_portfolio_return`).
        2. Calcula-se a volatilidade anual (função `calculate_portfolio_volatility`).
        3. Computa-se o Sharpe Ratio (função `sharpe_ratio`).

    - Mantém-se apenas a simulação com maior Sharpe Ratio.

5. **Paralelização**

    Por se tratar de uma tarefa computacionalmente mais demandante, a execução do código pode levar um tempo considerável, especialmente ao lidar com um grande número de combinações e simulações. Assim, a fim de otimizar o tempo de execução, o código foi estruturado de forma a permitir a execução em paralelo, técnica que possibilita a execução simultânea de múltiplas tarefas, aproveitando melhor os recursos computacionais disponíveis. 
    
    Para isso, foi utilizada a biblioteca `concurrent.futures`, especificamente o módulo `ProcessPoolExecutor`, que permite a execução de funções em paralelo utilizando múltiplos processos.

    Para este projeto, o paralelismo foi aplicado entre as combinações de ativos, isto é, cada combinação de 25 ativos é processada em um processo separado. Com essa abordagem, a carga de trabalho é distribuída uniformemente entre os processos, permitindo que cada um execute sua parte da tarefa de forma independente e simultânea.
    

6. **Resultado final**

    Ao fim, o script exibe o Sharpe Ratio máximo encontrado e a alocação dos 25 ativos correspondentes com seus respectivos pesos, ordenados de forma decrescente.

    A saída abaixo é um exemplo do resultado obtido ao executar o código:

```
    Best Sharpe Ratio: 3.0202
    Assets and Weights (sorted):
    CSCO: 0.0998
    WMT: 0.0931
    CRM: 0.0908
    DIS: 0.0883
    V: 0.0758
    MCD: 0.0714
    AAPL: 0.0670
    IBM: 0.0556
    AXP: 0.0529
    NVDA: 0.0468
    AMZN: 0.0440
    CVX: 0.0360
    HON: 0.0320
    MSFT: 0.0276
    TRV: 0.0252
    SHW: 0.0173
    PG: 0.0158
    GS: 0.0155
    MRK: 0.0122
    HD: 0.0122
    JPM: 0.0096
    CAT: 0.0086
    KO: 0.0013
    NKE: 0.0006
    VZ: 0.0005
```

### Comparativo de Tempo de Execução
Por fins de comparação, foram realizados testes de tempo de execução com e sem paralelização. Para uma mesma máquina, cujo processador contém 6 núcleos, os resultados foram os seguintes:
- Com paralelização: cerca de **40 minutos**.
- Sem paralelização (sequencial): cerca de **4 horas e 35 minutos**.

Dessa forma, a utilização de paralelização proporcionou uma redução significativa no tempo de execução, tornando o processo mais eficiente e viável.

## Como Executar
1. Certifique-se de ter o Python 3.11 ou versões superiores instalado em sua máquina.
2. Clone este repositório em sua máquina local.
```bash
git clone https://github.com/leoscarlato/projeto_otimizacao_carteira.git
```
3. Crie um ambiente virtual e ative-o:
```bash
python -m venv env
env/Scripts/activate
```
4. Instale as dependências necessárias:
```bash
pip install -r requirements.txt
```
5. Faça download dos dados, executando o script `data_fetcher.py`:
```bash
python data_loader/data_fetcher.py
```
6. Com os dados baixados e as dependências instaladas, execute o script principal:
```bash
python main.py
```
7. Após a execução, o script exibirá os resultados dentro do terminal. 


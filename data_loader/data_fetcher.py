import os
import certifi
import yfinance

os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()
os.environ['CURL_CA_BUNDLE'] = certifi.where()

acoes = [
    "UNH", "GS", "MSFT", "HD", "V", "SHW", "MCD", "CAT", "AMGN", "AXP",
    "TRV", "CRM", "IBM", "JPM", "AAPL", "HON", "AMZN", "PG", "BA", "JNJ",
    "CVX", "MMM", "NVDA", "WMT", "DIS", "MRK", "KO", "CSCO", "NKE", "VZ"
]

try:
    data = yfinance.download(acoes, start="2024-08-01", end="2024-12-31")
    if data.empty:
        print("❌ Falha ao baixar dados: DataFrame vazio!")
    else:
        data_final = data['Close']
        data_final.to_csv('data_loader/acoes.csv')
        print("✅ Dados salvos com sucesso em 'data_loader/acoes.csv'.")
except Exception as e:
    print(f"❌ Erro ao baixar dados: {e}")

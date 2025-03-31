import requests

# Endpoint para obter detalhes de um produto específico
endpoint = "http://localhost:8000/api/products/1/"

# Fazendo a requisição GET
response = requests.get(endpoint)

# Imprimindo os dados encontrados
data = response.json()
print("\nDados do produto:")
print(data) 
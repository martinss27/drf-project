import requests

endpoint = "http://localhost:8000/api/products/2123871/" #this is a non-existent endpoint

response = requests.get(endpoint)

data = response.json()

print(data) 
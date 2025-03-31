import requests

endpoint = "http://localhost:8000/api/products/2/"

response = requests.get(endpoint)

data = response.json()
print("\nproduct data:")
print(data) 
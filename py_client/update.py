import requests

endpoint = "http://localhost:8000/api/products/2/update/"

data = { 
    'title': 'Smartphone (updated)',
    'price': 8000.00
}

response = requests.put(endpoint, json=data)

print(response.json()) 
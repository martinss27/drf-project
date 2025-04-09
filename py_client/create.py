import requests

x = {"Authorization": 'Bearer 75b427d3f3f841cc66ea1eda53f0a9c979a82bdf'}

endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "this field is created just if have an authorization ",
    "price": 7331
}

get_response = requests.post(endpoint, json=data, headers=x)
print(get_response.json())
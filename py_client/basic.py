import requests

#endpoint = "https://httpbin.org/status/200"
#endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/" #http://localhost:8000/api/

get_response = requests.post(endpoint, json={"title": "None", "content": "hello world",
                                             "price": 30}) # HTTP Request

#print(get_response.text) # print raw text response
#print(get_response.status_code)

try:
    print(get_response.json())
except requests.exceptions.JSONDecodeError as e:
    print(f"Erro ao decodificar JSON: {e}")
    print(f"Resposta recebida: {get_response.text}")

# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# JavaScript Object Nototion ~ Python Dict


import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/api/auth/" #this is the endpoint to get the token
username = input("What is your username?\n ")
password = getpass("What is your password?\n") #getpass is a method that allows the script to read a password without displaying it visibly; I used it for security purposes

auth_response = requests.post(auth_endpoint, json={'username': username, 'password': password}) #this is the request to get the token
print(auth_response.json()) #this will print the response from the server


if auth_response.status_code == 200: #heck if the auth_response was successful.
    token = auth_response.json()['token'] #Capture the token generated if the user is authenticated
    headers = {
        "Authorization": f'Bearer {token}' #Include the token in the request headers
    }


    endpoint = "http://localhost:8000/api/products/"

    get_response = requests.get(endpoint, headers=headers) #this will get the data from the endpoint and pass our `headers` as headers
    print(get_response.json()) #this will print the data from the endpoint
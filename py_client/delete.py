import requests

product_id = input('what is the Product ID you want to use?: \n') #Collect which ID the user wants to delete

try:
    product_id = int(product_id) #Try to convert the input to an integer
except: #If it fails (e.g., the user entered 'abc' instead of an ID
    product_id = None #The product becomes None (null/invalid).
    print(f"Product ID {product_id} isn't valid.") #Error message informing the invalid format

if product_id: # If Product ID is True, execute the endpoint normally.
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"

    response = requests.delete(endpoint)
    print(response.status_code, response.status_code==204) 
import json
from django.http import JsonResponse
from products.models import Product
from django.forms.models import model_to_dict

def api_home(request, *args, **kwargs): #*args, **kwargs -> argumentos posicionais e argumentos nomeados
    # request _> HttpRequest -> Django
    #print(dir(request))
    #request.body
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    
    if model_data:
        data = model_to_dict(model_data)  
    return JsonResponse(data)


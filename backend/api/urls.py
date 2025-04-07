from django.urls import path
from .views import api_home
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.api_home), #Because the first parameter was empty, the URL will remain 'localhost:8000/api/' with nothing after 'api'
    # path('api/products', include('peoducts.url')) 
    path('auth/', obtain_auth_token) #this will create a new endpoint for us to get a token
]

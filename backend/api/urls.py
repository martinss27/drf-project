from django.urls import path
from .views import api_home
from . import views

urlpatterns = [
    path('', views.api_home), #Because the first parameter was empty, the URL will remain 'localhost:8000/api/' with nothing after 'api'
    # path('api/products', include('peoducts.url')) 
]

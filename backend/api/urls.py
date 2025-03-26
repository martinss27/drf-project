from django.urls import path
from .views import api_home

urlpatterns = [
    path('', api_home) #Because the first parameter was empty, the URL will remain 'localhost:8000/api/' with nothing after 'api'
]

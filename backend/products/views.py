from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['POST'])
def product_create(request):
    data = request.data
    print(data)
    return Response(data, status=status.HTTP_201_CREATED)

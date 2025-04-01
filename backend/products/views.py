from rest_framework import generics

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        #serializer.save(user=self.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None  
        if content is None:
            content = title
        serializer.save(content=content)
        # send a Django signal

product_list_create_view = ProductListCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #lookup_field = 'pk' 

product_detail_view = ProductDetailAPIView.as_view()


@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == 'GET':
        if pk is not None:
            #detail view
            obj = get_object_or_404(Product, pk=pk) #Look for the product by ID; if not found, return 404.
            data = ProductSerializer(obj, many=False).data #Convert only this specific product to JSON, passing in that object with `many=False` (which is the default, so we don’t need to declare it).
            return Response(data) #then we return the data
        #list view
        #And if there is no `pk`, it means we want all products.
        #For example, if someone accesses `/api/products/`, it means they want all products.
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data #Convert all products to JSON | The `many=True` here indicates that we want to convert multiple products.
        return Response(data)

    if method == 'POST':
        #create an item
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None  
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data, status=201)
    return Response({"invalid": "not good data"}, status=400)

'''Here, some code recycling occurred in the POST method.  

For example, lines 51, 52, 58, and 59 are the same as lines 13, 14, 18, and 19 in the `api/views.py` file.  

From lines 51 to 57, we can see that the code is the same as lines 17 to 21.  

In other words, for the POST method, we reused some lines of code from other places to save time and reduce redundancy.'''

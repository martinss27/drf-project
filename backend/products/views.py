from rest_framework import generics, mixins

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

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' 

    def perform_update(self, serializer):
        instance = serializer.save() #Save the changes and return the updated object.
        if not instance.content: #Check if the value is falsy; besides None, verify if it is "", False, 0, or []. This makes it more comprehensive and covers all fields.
            instance.content = instance.title #After checking if `content` is empty, if it is, assign the value of `title` to `content`.
            instance.save() #Since the `content` check happens after the save, I need to save again to persist the change.

product_update_view = ProductUpdateAPIView.as_view()

class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self,instance): #recebe um parametro instance, que é o obj que será destruido
        #perform destroy é como um gancho, que o framework fornece para que eu possa fazer coisas antes da deleção real acontecer
        super().perform_destroy(instance) #chama  perform_destroy da classe pai (através de super()) para execultar o DELETE real do obj
        '''se nao chamasse super().perform_destroy(instance) o obj nunca seria realmente deletado
        porque estaria sobrescrevendo o método sem executar a parte que realmente deleta'''


product_destroy_view = ProductDestroyAPIView.as_view()

class ProductMixinView(
    mixins.DestroyModelMixin, #Allows deleting a specific object
    mixins.ListModelMixin, #Allows listing all objects os objetos 
    mixins.CreateModelMixin, #Allows creating a new object
    mixins.UpdateModelMixin, #Allows updating a specific object
    mixins.RetrieveModelMixin, #Allows retrieving a specific object
    generics.GenericAPIView): #Allows using the list and retrieve methods

    queryset = Product.objects.all() #Queryset is the set of objects that will be listed or retrieved   
    serializer_class = ProductSerializer #`serializer_class` is the serializer that will be used to convert objects into JSON
    lookup_field = 'pk' #`lookup_field` is the field that will be used to retrieve a specific object (if applicable)

    def get(self,request, *args, **kwargs): #HTTP GET is the method that will be used to retrieve the objects
        print(args, kwargs) #Prints the arguments passed to the method
        pk = kwargs.get("pk") #Gets the `pk` from the URL
        if pk is not None: #Checks if `pk` exists in `kwargs` (a dictionary `{}`); if `pk` is not `None`, calls the `retrieve` method
            return self.retrieve(request, *args, **kwargs) #Calls the `retrieve` method
        return self.list(request, *args, **kwargs) #This `return` acts as an 'else' for the 'if', meaning that if there is no `pk`, it calls `self.list` and lists all products
    '''URL: `api/products/` → `kwargs` is `{}` (without `pk`), so it calls the `list` method.  
       URL: `api/products/1/` → `kwargs` is `{'pk': 1}` (with `pk`), so it calls the `retrieve` method.'''
    
    def post(self,request, *args, **kwargs): #HTTP POST is the method that will be used to create a new object
        return self.create(request, *args, **kwargs) #Calls the `create` method
    
    def perform_create(self, serializer): #This method is called when the `create` method is called
        content = serializer.validated_data.get('content') or None  #Gets the `content` from the validated data
        if content is None:
            content = 'this is a single view doing cool stuff' #If `content` is `None`, assign the value of `title` to `content`
        serializer.save(content=content) #Saves the `content` to the database   

    def update(self,request, *args, **kwargs): #HTTP PUT is the method that will be used to update an object
        return self.partial_update(request, *args, **kwargs) #Calls the `partial_update` method
    
    def perform_update(self, serializer):
        instance = serializer.save() #Save the changes and return the updated object.
        if not instance.content: #Check if the value is falsy; besides None, verify if it is "", False, 0, or []. This makes it more comprehensive and covers all fields.
            instance.content = instance.title #After checking if `content` is empty, if it is, assign the value of `title` to `content`.
            instance.save() #Since the `content` check happens after the save, I need to save again to persist the change.

    
    def delete(self,request, *args, **kwargs): #HTTP DELETE is the method that will be used to delete an object
        return self.destroy(request, *args, **kwargs) #Calls the `destroy` method
    
    def perform_destroy(self, instance): #This method is called when the `destroy` method is called
        super().perform_destroy(instance) #Calls the `destroy` method of the parent class


product_mixin_view = ProductMixinView.as_view()

@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == 'GET':
        if pk is not None:
            #detail view
            obj = get_object_or_404(Product, pk=pk) #Look for the product by ID; if not found, return 404.
            data = ProductSerializer(obj, many=False).data #Convert only this specific product to JSON, passing in that object with `many=False` (which is the default, so we don't need to declare it).
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


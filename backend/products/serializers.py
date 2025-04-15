from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field= 'pk'
        )
    delete_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'delete_url',
            'url',
            'edit_url',
            'pk',
            'title',
            'content',
            'price',
            'my_discount'
        ]

    def get_edit_url(self,obj): #Method automatically called by DRF to generate the value of the url field (due to SerializerMethodField). (self = serializer), (obj = instance of the Product model being serialized at the moment).
        request = self.context.get('request') #self.context is a dictionary that handles information outside the model (in this case, the request, which is not part of the Product model). //////// hosturlpart   /normal part
                                              #In this case, the reverse function needs to be called with the request to return the full URL (including the host domain)                     http://localhost:8000/api/products/5/

        
        if request is None: #Just a safety check — if request is None, it returns None to avoid an error
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)
# reverse params   |viewname(from urls.py)| #keyword args (obj.pk) | 

    def get_delete_url(self,obj):
        x = self.context.get('request')

        if x is None:
            return None
        return reverse('product-delete', kwargs={"pk": obj.id}, request=x)
        '''
        ⬆️ Here I used reverse to generate the URL corresponding to the view (in this case, product-detail). 
        The kwargs argument is used to fill in the <int:pk> part of the URL — that is, the product ID (by default, the URL would look like: /api/products/5/). 
        It captures the pk from the URL. Then I pass the request as an argument — DRF uses the current request’s information (domain and protocol) to build a complete URL, like: 
        http://localhost:8000/api/products/5/
        '''  

    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_my_discount()

'''
# url = serializers.SerializerMethodField(read_only=True)
#  def get_url(self, obj):
#     return f'/api/v2/products/{obj.pk}/' 

This is a method to reference the specific URL of a product. 
When working with a single model and a single serializer, this is usually not a big issue (I mean, these lines are already sufficient).
However, when dealing with larger applications, we need to modify this get_url method to make it more effective.'''
from rest_framework.routers import DefaultRouter

from products.viewsets import ProductGenericViewSet

router = DefaultRouter()
router.register('products-v2', ProductGenericViewSet, basename='products-v2')


print(router.urls)
urlpatterns = router.urls

'''This part using the default router was just to make it work with the viewset, 
but it's not something I particularly enjoy doing or feel I should adopt as a habit. 
I don't use it much because I miss having full control over the URLs. 
Personally, I prefer using regular URL patterns because I like to define exactly what they are and where they go.'''
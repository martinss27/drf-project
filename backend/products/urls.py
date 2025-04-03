from django.urls import path
from .views import ProductListCreateAPIView, ProductUpdateAPIView, ProductDestroyAPIView, ProductMixinView
from . import views

urlpatterns = [
    path('', views.product_mixin_view), #/api/products
    path('<int:pk>/', views.product_mixin_view), #/api/products/id
    path('<int:pk>/update/', views.product_update_view), #api/products/id/update
    path('<int:pk>/delete/', views.product_destroy_view) #api/products/id/delete
]
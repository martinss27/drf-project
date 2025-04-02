from django.urls import path
from .views import ProductListCreateAPIView, ProductUpdateAPIView
from . import views

urlpatterns = [
    path('', views.product_list_create_view), #/api/products
    path('<int:pk>/', views.product_detail_view),
    path('<int:pk>/update/', views.product_update_view),
]
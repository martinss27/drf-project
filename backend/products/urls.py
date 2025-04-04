from django.urls import path
from .views import product_list_create_view, product_detail_view, product_update_view, product_destroy_view
from . import views

urlpatterns = [
    path('', views.product_list_create_view), #/api/products/
    path('<int:pk>/', views.product_detail_view), #/api/products/id
    path('<int:pk>/update/', views.product_update_view), #api/products/id/update
    path('<int:pk>/delete/', views.product_destroy_view) #api/products/id/delete
]
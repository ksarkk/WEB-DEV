from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.get_categories, name='get_categories'),
    path('categories/<int:pk>/', views.get_category, name='get_category'),
    path('products/', views.get_products, name='get_products'),
    path('products/<int:pk>/', views.get_product, name='get_product'),
    path('categories/<int:pk>/products/', views.get_products_by_category, name='gpbc')
]
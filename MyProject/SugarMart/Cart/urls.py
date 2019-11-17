from django.urls import path, include
from .views import create_cart#, remove_cart

urlpatterns = [
    path('cat/<int:pk>/', create_cart, name='cat'),
    #path('remove/<int:pk>/', create_cart, name='remove'),


]
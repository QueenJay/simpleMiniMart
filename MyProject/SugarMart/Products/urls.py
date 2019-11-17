from django.urls import path, include
from .views import ProductListView, ProductDetailView, ProductCreateView, CartListView#, ProductUpdateView

urlpatterns = [
    path('list/', ProductListView.as_view(), name= 'product_list'), #listView For the products
    path('create/', ProductCreateView.as_view(), name= 'create_list'),
    path('cart/', CartListView.as_view(), name= 'cart'),
    path('list/<int:pk>/', ProductDetailView.as_view(), name= 'product_detail'), #detailView for the products

]
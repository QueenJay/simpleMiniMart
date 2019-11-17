from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from .models import ProductsMode
from Cart.models import CartMode
from django.views.generic import ListView, DetailView, CreateView, UpdateView

User = get_user_model()
class ProductListView(ListView):
    # qs = ProductsMode.objects.all().first() 
    # qs_final = qs.update(active_me= True)
    queryset        =ProductsMode.objects.all() 

class ProductDetailView(DetailView):
    queryset        =ProductsMode.objects.all() 


class ProductCreateView(CreateView):
    model = ProductsMode 
    template_name = 'Products/trial.html'
    success_url = '/prod/list/'
    fields = ["title","description","price","image","featured"]

class ProductFeaturedListView(ListView):
    template_name = "Products/productsmode_list.html"

    def get_queryset(self, *args, **kwargs): 
        request     =self.request
        return ProductsMode.objects.featured() 

class ProductProductFeaturedDetailView(DetailView):
    template_name = "Products/featured_detail.html" 

    def get_queryset(self, *args, **kwargs): 
        request     =self.request
        return ProductsMode.objects.featured() 

class CartListView(ListView):
    template_name = "products/cart_list.html" 

    def get_queryset(self):
        chart_list =self.request.user
        queryset   =CartMode.objects.filter(user__iexact = chart_list)
        return queryset
        
    
    
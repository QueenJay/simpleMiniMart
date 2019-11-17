from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from .models import CartMode
from Products.models import ProductsMode
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView


class CartDetail(DetailView):
    success_url = '/prod/list/'

User = get_user_model()
def create_cart(request, pk ):
    qs          = ProductsMode.objects.filter(pk = pk).first()
    qs_present  = CartMode.objects.filter(Products__iexact = qs.title , user__iexact = request.user).first()
    
    if qs_present :
        pass
    else:
        user  = request.user
        product =qs.title
        subtotal = qs.price

        use_me = CartMode.objects.create(user = user, Products = product, subtotal = subtotal)
        use_me.send_confirmation_email()


    return HttpResponseRedirect("/prod/list/")

# def remove_cart(request, pk ):
#     qs_here = CartMode.objects.filter(id = pk).first()
    
#     if qs_here.exists():
#     #     user  = request.user
#     #     product =qs.title
#     #     subtotal = qs.price

#         CartMode.objects.remove(qs_here)
#     else:
#         pass
    
#     return HttpResponseRedirect("/prod/list/")

class CartCreateView(CreateView):
    model = CartMode 
    template_name = 'Cart/trial.html'
    success_url = '/prod/list/'
    fields = ["user","Products","subtotal"]

    def form_valid(self, form, *args, **kwargs):
        instance = form.save(commit=False)
        #instance.owner=self.request.user
        print (instance.pk)
        return super(CartCreateView,self).form_valid(form)


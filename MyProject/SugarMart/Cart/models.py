from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from Products.models import ProductsMode
from django.db.models.signals import pre_save
#import random


class CartMode(models.Model):
    user        =models.CharField(max_length = 130 )
    Products    =models.CharField(max_length = 130 )
    subtotal    =models.DecimalField(decimal_places=2, max_digits=20)
    timestamp   =models.DateTimeField(auto_now_add = True) 
    updated     =models.DateTimeField(auto_now = True)

    #objects     =ProductsModeManager

    def __str__(self):
        return self.Products
 
    def get_absolute_url(self):
        return self.pk

    def send_confirmation_email(self):
        print("Cart created!")
        pass


# def rl_pre_save_receiver(sender, instance, *args, **kwargs):
#     qs = ProductsMode.objects.filter(active_me = True).first()
#     instance.Products = instance.Products.set(qs)

    
# pre_save.connect(rl_pre_save_receiver, sender=CartMode)
from django.db import models
#import random




class ProductsMode(models.Model):
    title       =models.CharField(max_length = 128)
    description =models.TextField()
    price       =models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    image       =models.FileField( upload_to = 'static/img', null = True, blank = True)
    timestamp   =models.DateTimeField(auto_now_add = True) 
    updated     =models.DateTimeField(auto_now = True)

    #objects     =ProductsModeManager

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return self.pk
from django.shortcuts import render
from Cart.models import CartMode
from django.contrib.auth import get_user_model


User = get_user_model()
def CheckoutDetail(request):
    template_name= "Checkout/checkdetail.html"
    Amount = 0.00

 #getting the only active user. get()isn't user to avoid errors when there is no active_user
    cart_all = CartMode.objects.filter(user = request.user)#filtering objects for the active user only
    for obj in cart_all:
        product_price = obj.subtotal
        Amount = Amount + float(product_price)
    shipping_price = 100
    Total_price = Amount + float(shipping_price)
    
    context = {
        "Subtotal" : Amount,
        "Shipping_charge" : shipping_price,
        "Total" : Total_price
    }

    return render(request, template_name, context) 

        


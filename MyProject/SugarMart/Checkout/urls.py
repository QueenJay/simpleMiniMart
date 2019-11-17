from django.urls import path, include
from .views import CheckoutDetail

urlpatterns = [
    path('check/', CheckoutDetail, name='checkout'),
    # path('carrt/', CartCreateView.as_view(), name='carrt'),
    # path('about/', about_page, name='abouta'),
    # path('login/', login_page, name='login'),
    # path('register/', register_page, name='register'),


]
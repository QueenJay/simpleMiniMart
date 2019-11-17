from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from .views import about_page, contact_page, login_page, register_page

urlpatterns = [
    
    path('logout/',LogoutView.as_view(), name='logout'),
    #path('login/',LoginView.as_view(), name='login'),
    path('contact/', contact_page, name='contacta'),
    path('about/', about_page, name='abouta'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    #path('about/', about_page, name='abouta'),
    #path('login/', login_page, name='login'),
    #path('register/', register_page, name='register'),


]
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from .forms import ContactForm, LoginForm, RegisterForm

def about_page(request):
    context = {
        "title":"About",
        "content":"Welcome to about page",
    }
    return render(request, "basics/about.html" , context)

def contact_page(request):
    context = {
        "title":"contact",
        "content":"Welcome to contact page",
        "form": ContactForm 
    }
    return render(request, "basics/contact.html" , context)

def login_page(request):
    template_name = "auth/login.html"
    form = LoginForm(request.POST or None)
    context = {
        "form":form,
        }
    #print(request.user.is_authenticated)
    #username = request.POST.get('username')

    if form.is_valid():
        #print(form.cleaned_data)
        username    =form.cleaned_data.get("username")
        password    =form.cleaned_data.get("password")
        username    =authenticate(request, username=username, password=password)

        if username is not None:
            login(request, username) #this method is very essential
            return redirect("/basic/about/")
        else:
            print("Error?")
        

    return render(request, template_name, context)

User = get_user_model()
def register_page(request):
    template_name = "auth/register.html"
    form = RegisterForm(request.POST or None)
    context = {
        "form" : form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("emaail")
        password = form.cleaned_data.get("password")
        User.objects.create_user(username, email, password)
        return redirect("/basic/about/")

    return render(request, template_name, context)
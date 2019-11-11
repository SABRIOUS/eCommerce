from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm, LoginForm

def home_page(request):
    context = {
        "title":"hello world!",
        "content": "Welcome To Home Page"
    }
    return render(request,'home_page.html',context)

def about_page(request):
    context = {
        "title":"About Page",
        "content": "Welcome To About Page"
    }
    return render(request,'home_page.html',context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title":"Contact",
        "content": "Welcome To Contact Page",
        "form":contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request,'contact/view.html',context)


def login_page(request):
    form = LoginForm(request.POST or None)
    print("User Logged In ... ")
    print(request.user.is_authenticated)
    context = {
        "form":form
    }
    if form.is_valid():
        print(form.cleaned_data)
    return render(request,"auth/login.html",context)


def register_page(request):
    return render(request,"auth/register.html",{})

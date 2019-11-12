from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,get_user_model
from django.http import HttpResponse
from .forms import ContactForm, LoginForm,RegisterForm

def home_page(request):
    context = {
        "title":"hello world!",
        "content": "Welcome To Home Page"
    }
    if request.user.is_authenticated:
        context["premium_content"] = "YEAHHHHHHHHHH"
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
    context = {
        "form":form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            #clear the form
            # context['form'] = LoginForm()
            # Redirect to a sccess page.
            return redirect("/")
        else:
            print("Error... ")
            # Return and 'invalid login' error message
    return render(request,"auth/login.html",context)

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form":form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        new_user = User.objects.create_user(username,email,password)
        print(new_user)
    return render(request,"auth/register.html",context)

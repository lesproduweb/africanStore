from django.contrib.auth import authenticate, login, get_user_model, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import LoginForm, ResgisterForm, ContactForm
import os
from os import listdir
from os.path import isfile, join
from .settings import BASE_DIR


def home_page(request):
    #print(f"base dir: {BASE_DIR}")
    # onlyfiles = ["img/"+f for f in listdir("/home/dev/Black-Maket/blackmaket/src//static_my_project/img") if isfile(join("/home/dev/Black-Maket/blackmaket/src/static_my_project/img", f))]
    # return render(request, 'home_page.html', {"files": onlyfiles})
    return render(request, 'home_page.html', {})

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect("/")

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            #print(request.user.is_authenticated)
            login(request, user)
            # Redirect to a success page.
            context['form'] = LoginForm()
            return redirect("/")
        else:
            # Return an 'invalid login' error message.
            # ...
            return render(request, "auth/login.html", context)
            # raise form.ValidationError("Authentification incorecte")
    return render(request, "auth/login.html", context)


User = get_user_model()
def register_page(request):
    form = ResgisterForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
        login(request, new_user)
        # return render(request, "auth/register.html", context)
        return redirect("/")
    return render(request, "auth/register.html", context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title":"Contact",
        "content":" Welcome to the contact page.",
        "form": contact_form,
        "title_name": "Contact",
        "brand_name": "Contact"
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == "POST":
    #     #print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request, "contact/view.html", context)

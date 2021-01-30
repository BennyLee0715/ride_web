from django.http import HttpResponse
from django.shortcuts import render,redirect
from . import models
from .form import LoginForm, RegisterForm

def home(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        message = "Please check again！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    return redirect('/chooseCharacter/')
                else:
                    message = "Incorrect password！"
            except:
                message = "User does not exist！"
        return render(request, 'home.html', locals())

    login_form = LoginForm()
    return render(request, 'home.html', locals())

def register(request):
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "Please try again！"
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password = register_form.cleaned_data['password']
            email = register_form.cleaned_data['email']
            try:
                models.User.objects.get(name=username)
                message = "User has already existed!"
                return render(request, 'register.html', locals())
            except:
                # user name is new
                models.User(name = username, password = password, email = email).save()
                return redirect('home/')
    register_form = RegisterForm()
    return render(request, 'register.html', locals())
def chooseCharacter(request):

    return render(request, 'chooseCharacter.html')

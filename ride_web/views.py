from django.http import HttpResponse
from django.shortcuts import render,redirect
from . import models
from .form import LoginForm

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

def chooseCharacter(request):

    return render(request, 'chooseCharacter.html')

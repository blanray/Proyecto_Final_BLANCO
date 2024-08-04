from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .forms import *
from django.contrib.auth import login, logout, authenticate

def register(request):
       
    if request.method=='POST':
        miForm = UserRegisterForm(request.POST)

        if miForm.is_valid():
            miForm.save()
            return redirect(reverse('index'))
        else:
             messages.error(request, 'Error registrando el usuario')
             miForm = UserRegisterForm()

    else:
        miForm = UserRegisterForm()

    return render(request, './Users/register.html', {"miForm": miForm})

def login_user(request):
       
    if request.method=='POST':
        miForm = UserLoginForm(request, data=request.POST)

        if miForm.is_valid():

            usuario = miForm.cleaned_data.get('username')
            passw = miForm.cleaned_data.get('password')

            user = authenticate(username = usuario, password = passw)

            if user is not None:
                login(request, user)
                return redirect(reverse('index'))
            else:
                messages.error(request, 'Error iniciando sesion')
                miForm = UserLoginForm()
        
        else:
             messages.error(request, 'Error iniciando sesion')
             miForm = UserLoginForm()


    else:
        miForm = UserLoginForm()

    return render(request, './Users/login.html', {"miForm": miForm})
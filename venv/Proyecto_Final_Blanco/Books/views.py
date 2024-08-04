from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .models import *
#from .forms import *

def inicio(request):

    if request.method == 'POST':
        pass
    else:
        pass
    
    return render(request, 'Books/inicio.html')

def about(request):
    return render(request, 'Books/about.html')
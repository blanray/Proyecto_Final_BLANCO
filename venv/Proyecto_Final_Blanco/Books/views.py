from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from .models import *
from .forms import *

def inicio(request):

    if request.method == 'POST':
        pass
    else:
        pass
    
    return render(request, 'Books/inicio.html')

def about(request):
    return render(request, 'Books/about.html')

@login_required
def books(request):
    books = Book.objects.all()
    return render(request, 'Books/books.html', {'books': books})

@login_required
def bookDetail(request, idBook):

    print(f"Busco id {idBook}")
    book = Book.objects.get(id=idBook)

    print(book)

    return render(request, 'Books/bookDetail.html', {'book': book})

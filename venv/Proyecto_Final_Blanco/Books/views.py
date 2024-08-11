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
    book = Book.objects.get(id=idBook)

    return render(request, 'Books/bookDetail.html', {'book': book})

@login_required
def bookInsert(request):

    if request.user.is_superuser:
        
        if request.method=='POST':
            miForm = BookForm(request.POST, request.FILES)

            if miForm.is_valid():
                miFormTemp = BookForm(request.POST, request.FILES)
                bookTemp = miFormTemp.save(commit=False)
                bookTemp.save()
                messages.success(request, 'Libro registrdo correctamente')
                return redirect(reverse('books'))
            else:
                messages.error(request, 'Error registrando el libro')
                miForm = BookForm()

        else:
            miForm = BookForm()

        return render(request, 'Books/bookInsert.html', {'miForm': miForm})
    else:
        messages.error(request, "No tiene permisos para acceder a esa pagina")
        return redirect(reverse('index'))

@login_required
def bookEdit(request, pk):

    if request.user.is_superuser:
        
        if request.method=='POST':
            miForm = BookForm(request.POST, request.FILES)

            if miForm.is_valid():
                bookTemp = Book.objects.get(id=pk)
                miFormTemp = BookForm(request.POST, request.FILES, instance = bookTemp)
                miFormTemp.save()
                messages.success(request, 'Libro actualizado correctamente')
                return redirect(reverse('books'))
            else:
                messages.error(request, 'Error registrando el libro')
                miForm = BookForm()

        else:
            bookTemp = Book.objects.get(id=pk)
            miForm = BookForm(instance = bookTemp)

        return render(request, 'Books/bookEdit.html', {'miForm': miForm, 'book': bookTemp})
    else:
        messages.error(request, "No tiene permisos para acceder a esa pagina")
        return redirect(reverse('index'))

@login_required
def bookDelete(request, pk):

    if request.user.is_superuser:
        try:
            book = Book.objects.get(id=pk)
            book.delete()
            messages.success(request, 'Libro eliminado exitosamente')
        except:
            pass
    else:
        messages.error(request, "No tiene permisos para eliminar libros")

    return redirect(reverse('books'))
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from .models import *
from .forms import *
from datetime import datetime
from django.template.defaulttags import register

@register.filter
def get_range(value):
    return range(value)


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
    valoraciones = Review.objects.filter(book__id = idBook)

    return render(request, 'Books/bookDetail.html', {'book': book, 'cantidadValoraciones': len(valoraciones), 'reviews': valoraciones})

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

@login_required
def reviewInsert(request, bookId):

    if request.method=='POST':
        miForm = ReviewForm(request.POST)

        if miForm.is_valid():
            miFormTemp = ReviewForm(request.POST)
            reviewTemp = miFormTemp.save(commit=False)
            reviewTemp.user = request.user
            bookTemp = Book.objects.get(id = bookId)
            reviewTemp.book = bookTemp
            reviewTemp.save()
  
            messages.success(request, 'Valoración registrada correctamente')
            return redirect(reverse('books'))
        else:
            messages.error(request, 'Error registrando la valoración')
            miForm = ReviewForm()

    else:
        miForm = ReviewForm()

    return render(request, 'Books/reviewInsert.html', {'miForm': miForm})

@login_required
def reviewDelete(request, pk):

    miReviewTemp = Review.objects.get(id = pk)

    if (request.user == miReviewTemp.user) or (request.user.is_superuser):
        try:
            miReviewTemp.delete()
            messages.success(request, 'Comentario eliminado exitosamente')
        except:
            pass
    else:
        messages.error(request, "No tiene permisos para eliminar valoraciones de otro usuario")

    return redirect(reverse('books'))

@login_required
def reviewEdit(request, pk):

    miReviewTemp = Review.objects.get(id = pk)

    if (request.user == miReviewTemp.user):
        
        if request.method=='POST':
            miForm = ReviewForm(request.POST)

            if miForm.is_valid():
                miReviewTemp.created = datetime.now()
                miFormTemp = ReviewForm(request.POST, instance = miReviewTemp)
                miFormTemp.save()
                messages.success(request, 'Valoracion actualizada correctamente')
                return redirect(reverse('books'))
            else:
                messages.error(request, 'Error registrando la valoracion')
                miForm = ReviewForm(instance = miReviewTemp)

        else:
            miForm = ReviewForm(instance = miReviewTemp)

        return render(request, 'Books/reviewEdit.html', {'miForm': miForm, 'review': miReviewTemp})
    else:
        messages.error(request, "No tiene permisos para acceder a esa pagina")
        return redirect(reverse('index'))

@login_required
def reviews(request):

    if request.method == 'POST':
        miOrden = request.POST.get('order', 'Nuevas')
        miFiltro = request.POST.get('filter', 'Todas')
    
        if miOrden == 'Nuevas':
            reviews = Review.objects.all().order_by('-created')
        else:
            reviews = Review.objects.all().order_by('created')

        if miFiltro == 'Mias':
            reviews = Review.objects.all().filter(user = request.user)

        miForm = ReviewMenu(request.POST)    
    else:
        reviews = Review.objects.all()
        miForm = ReviewMenu() 
    
    return render(request, 'Books/reviews.html', {'reviews': reviews, 'miForm': miForm})

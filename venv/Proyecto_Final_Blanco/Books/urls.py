from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name = 'index'),
    path('about', views.about, name = 'about'),
]

books = [
    path('books', views.books, name = 'books'),
    path('bookDetail/<idBook>', views.bookDetail, name = 'bookDetail'),
    path('bookInsert', views.bookInsert, name = 'bookInsert'),
]

urlpatterns += books

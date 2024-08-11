from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name = 'index'),
    path('about', views.about, name = 'about'),
]

books = [
    path('books', views.books, name = 'books'),
    path('bookDetail/<idBook>', views.bookDetail, name = 'bookDetail'),
    path('bookEdit/<pk>', views.bookEdit, name = 'bookEdit'),
    path('bookDelete/<pk>', views.bookDelete, name = 'bookDelete'),
    path('bookInsert', views.bookInsert, name = 'bookInsert'),
]

reviews = [
    path('reviewInsert/<bookId>', views.reviewInsert, name = 'reviewInsert'),
]


urlpatterns += books

urlpatterns += reviews


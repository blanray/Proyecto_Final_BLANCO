from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 

class Book(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    author = models.CharField(max_length=50, null=False, blank=False)
    image = models.ImageField(upload_to='portadas', null=False, blank=False)

    def __str__(self):
        return f'Book | Id: {self.id} - Nombre: {self.name} - Autor: {self.author}'


class Review(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    comment = models.TextField(max_length=150, null=False, blank=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=5, choices=((i,i) for i in range(0, 6)))
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review | Id: {self.id} - Detalle: {self.comment} - Creado por: {self.user} - Libro: {self.book} - Rating: {self.rating} - Fecha: {self.created}'


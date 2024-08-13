from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["name", "author", "description", "image"]
        help_text = {k: "" for k in fields}

class ReviewForm(ModelForm):
    
    class Meta:
        model = Review
        fields = ["comment", "rating"]
        help_text = {k: "" for k in fields}

class ReviewMenu(forms.Form):
    ordenar=[('Antiguas','Mas antiguas primero'), ('Nuevas', 'Mas recientes primero')]

    filtro= [('Todas', 'Todas las valoraciones'), ('Mias', 'Solo mis valoraciones')]

    order = forms.ChoiceField(choices=ordenar, label="Ordenada por")

    filter = forms.ChoiceField(choices=filtro, label="Mostrar")

    class Meta:
        model = Review
        fields = ["order", "filter"]
        help_text = {k: "" for k in fields}
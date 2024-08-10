from django import forms
from django.contrib.auth.models import User
from .models import *

class BookForm(forms.Form):
    class Meta:
        model = Book
        exclude = ["id"]

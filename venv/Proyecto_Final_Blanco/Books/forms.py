from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["name", "author", "description", "image"]
        help_text = {k: "" for k in fields}

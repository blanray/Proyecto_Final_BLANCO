from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Creo mis formularios personalizados que heredan del propio de Django y de Forms

class UserRegisterForm(UserCreationForm, forms.Form):
    username = forms.CharField(label="Ingrese username", max_length=30, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'username',
        }
    ))
    email= forms.EmailField(label="Ingrese email", widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'email',
        }
    ))
    last_name = forms.CharField(label="Ingrese nombre del usuario", max_length=30, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'nombre del usuario',
        }
    ))
    first_name = forms.CharField(label="Ingrese apellido del usuario", max_length=30, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'apellido del usuario',
        }
    ))
    password1 = forms.PasswordInput(attrs={
            'class': 'form-control'
        })
    password2 = forms.PasswordInput(attrs={
            'class': 'form-control'
        })

    class Meta:
        model = User
        fields = ["username", "last_name", "first_name", "email", "password1", "password2"]
        help_text = {k: "" for k in fields}

class UserLoginForm(AuthenticationForm, forms.Form):

    username = forms.CharField(label="Ingrese username", max_length=30, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'username',
        }
    ))
    password = forms.PasswordInput(attrs={
            'class': 'form-control'
        })

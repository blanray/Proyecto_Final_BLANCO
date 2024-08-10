from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from .forms import *


def register_user(request):
       
    if request.method=='POST':
        miForm = UserRegisterForm(request.POST)

        if miForm.is_valid():
            miForm.save()
            messages.success(request, 'Usuario registrdo correctamente')
            return redirect(reverse('index'))
        else:
             messages.error(request, 'Error registrando el usuario')
             miForm = UserRegisterForm()

    else:
        miForm = UserRegisterForm()

    return render(request, './Users/register.html', {"miForm": miForm})

def login_user(request):
       
    if request.method=='POST':
        miForm = UserLoginForm(request, data=request.POST)

        if miForm.is_valid():

            usuario = miForm.cleaned_data.get('username')
            passw = miForm.cleaned_data.get('password')

            user = authenticate(username = usuario, password = passw)

            if user is not None:
                login(request, user)
                messages.success(request, 'Sesion iniciada correctamente')
                return redirect(reverse('index'))
            else:
                messages.error(request, 'Error iniciando sesion')
                miForm = UserLoginForm()
        
        else:
             messages.error(request, 'Error iniciando sesion')
             miForm = UserLoginForm()


    else:
        miForm = UserLoginForm()

    return render(request, './Users/login.html', {"miForm": miForm})

@login_required
def logout_user(request):
    logout(request)
    messages.success(request, 'Sesion cerrada')
    return redirect(reverse('index'))

@login_required
def update_user(request):
    
    miUser = request.user

    if request.method=='POST':
        miForm = UserUpdateForm(request.POST, instance=miUser)

        if miForm.is_valid():
            miForm.save()
            messages.success(request, 'Usuario actualizado correctamente')
            return redirect(reverse('index'))
        else:
            messages.error(request, 'Error actualizando el usuario')
            miForm = UserUpdateForm(instance=miUser)

    else:
        miForm = UserUpdateForm(instance=miUser)

    return render(request, './Users/update.html', {"miForm": miForm})

class PassUpdate(LoginRequiredMixin, PasswordChangeView):
    template_name='Users/updatePass.html'
    success_url = reverse_lazy('index')

@login_required
def update_avatar(request):
    
    miUser = request.user

    if request.method=='POST':
        miForm = AvatarUpdateForm(request.POST, request.FILES)

        if miForm.is_valid():

            if miForm.cleaned_data.get('image'):
                try:
                    miUser.avatar.image = miForm.cleaned_data.get('image')
                    miUser.avatar.save()
                except Avatar.DoesNotExist:
                    miAvatar = Avatar(miUser.id, miForm.cleaned_data.get('image'))
                    miUser.avatar = miAvatar
                    miUser.avatar.image = miForm.cleaned_data.get('image')
                    miUser.avatar.save()
            messages.success(request, 'Avatar actualizado correctamente')
            return redirect(reverse('index'))
        else:
            messages.error(request, 'Error actualizando el avatar')
            miForm = AvatarUpdateForm()

    else:
        miForm = AvatarUpdateForm()

    return render(request, './Users/updateAvatar.html', {"miForm": miForm})

@login_required
def admin_users(request):

    if request.user.is_superuser:
        User = get_user_model()
        usuarios = User.objects.all()
        return render(request, './Users/adminUsers.html', {"usuarios": usuarios})
    else:
        messages.error(request, "No tiene permisos para editar usuarios")
        return redirect(reverse('index'))

@login_required
def delete(request, userId):

    if request.user.is_superuser:
        try:
            user = User.objects.get(id=userId)
            user.delete()
            messages.success(request, 'Usuario eliminado exitosamente')
        except:
            pass
    else:
        messages.error(request, "No tiene permisos para eliminar usuarios")

    return redirect(reverse('index'))
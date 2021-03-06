from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

from .models import User
from .forms import UserRegister


def login_view(request):
    if request.user.is_authenticated:
        return redirect('posts:post')

    template_name = 'users/login.html'

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, f'Bienvenido {user.username}')
            return redirect('posts:post')
        else:
            messages.error(request, 'Usuario o Contraseña invalidos')

    return render(request, template_name)


def logout_view(request):
    logout(request)
    messages.success(request, 'Sesion cerrada exitosamente')
    return redirect('users:login')


def register(request):
    if request.user.is_authenticated:
        return redirect('posts:post')

    template_name = 'users/register.html'
    form = UserRegister(request.POST)

    if request.method == 'POST' and form.is_valid():
        user = form.save()

        if user:
            login(request, user)
            messages.success(request, f'La cuenta {user.username} fue creada exitosamente')
            return redirect('posts:post')

    return render(request, template_name, {
        'form': form,
    })

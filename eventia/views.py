from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

def loguear(request):
    error = None
    if request.method == 'POST':
        user = request.POST['user']
        passw = request.POST['password']     
        auth_user = authenticate(username = user,
        password = passw)
        if auth_user is not None:
            login(request, auth_user)
            return render(request, 'index.html')
        else:
            error = 'Usuario o contraseña incorrectos'
            return render(request, 'login.html', {'error': error})
    return render(request, 'login.html')

def homepage(request):
    return render(request, 'index.html')
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_view, logout as logout_view
from django.contrib import messages

def index(request):
    return render(request, 'core/index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_view(request, user)
            return redirect("/")
        else:
            messages.error(request, 'Invalid username or password')
    else:
        return render(request, 'core/login.html')

def logout(request):
    logout_view(request)
    return render(request, 'core/index.html')
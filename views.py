from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register_view(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Account created successfully!")
        return redirect('login')
    return render(request, 'core/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        passwd = request.POST.get('password')
        user = authenticate(request, username=uname, password=passwd)
        if user:
            login(request, user)
            return redirect('dashboard')
        messages.error(request, "Invalid credentials!")
    return render(request, 'core/login.html')

@login_required
def dashboard_view(request):
    return render(request, 'core/dashboard.html', {'role': request.user.role})

def logout_view(request):
    logout(request)
    return redirect('login')

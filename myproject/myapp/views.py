from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistrationForm
from .models import Users
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Users

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)  # Проверяем пароль
            if user is not None:
                login(request, user)  # Вход в систему
                if user.Role == 'admin':
                    return redirect('admin_page')
                elif user.Role == 'user':
                    return redirect('user_page')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Хешируем пароль
            user.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def admin_page(request):
    return render(request, 'admin_page.html')

def user_page(request):
    return render(request, 'user_page.html')
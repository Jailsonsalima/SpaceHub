from django.shortcuts import render, redirect

# Create your views here.

from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastro_sucesso')  # redireciona para a página de login
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/auth_page.html', {'form': form})


def auth_page(request):
    signup_form = CustomUserCreationForm()
    login_form = CustomAuthenticationForm()

    # Se for POST, decide qual formulário foi enviado
    if request.method == 'POST':
        if 'username' in request.POST and 'password1' in request.POST:
            # Cadastro
            signup_form = CustomUserCreationForm(request.POST)
            if signup_form.is_valid():
                signup_form.save()
                return redirect('cadastro_sucesso')  
        elif 'username' in request.POST and 'password' in request.POST:
            # Login
            login_form = CustomAuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                auth_login(request, user)
                return redirect('dashboard')  # redireciona para o dashboard após login

    return render(request, 'accounts/auth_page.html', {
        'signup_form': signup_form,
        'login_form': login_form
    })


def cadastro_sucesso(request):
    return render(request, 'accounts/cadastro_sucesso.html')

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('dashboard')  # redireciona para a home após login
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/auth_page.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    return redirect('home')



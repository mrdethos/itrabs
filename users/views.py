from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model, login as auth_login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm 
from .forms import UserRegistrationForm


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)        
            messages.success(request, f'Conta criada com sucesso')
            return redirect('/')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    else:
        form = UserRegistrationForm()
    return render(
        request=request,
        template_name='users/signup.html',
        context={'form': form}
    )

def login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Email ou senha inválido.")
        else:
            messages.error(request, "Email ou senha inválido.")
    form = AuthenticationForm()
    return render(
        request=request, 
        template_name='users/login.html',
        context={'form': form}
    )
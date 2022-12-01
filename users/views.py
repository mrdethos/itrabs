from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model, login as auth_login, authenticate, logout as auth_logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserLoginForm, UserUpdateForm


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
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
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('customer_profile', username)
            else:
                messages.error(request, "Usuário ou senha inválido.")
        else:
            messages.error(request, "Usuário ou senha inválido.")
    form = AuthenticationForm()
    return render(
        request=request, 
        template_name='users/login.html',
        context={'form': form}
    )

@login_required
def logout(request):
    auth_logout(request)
    return redirect('home')

def customer_profile(request, username):
    if request.method == 'POST':
        user = request.user
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user_form = form.save()
            return redirect('customer_profile', user_form.username)
    
    user = get_user_model().objects.filter(username=username).first()
    if user:
        form = UserUpdateForm(instance=user)
        return render(
            request=request,
            template_name='users/perfilcontratante.html',
            context={'form': form}
            )
    return redirect('home')

def professional_profile(request, username):
    if request.method == 'POST':
        user = request.user
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user_form = form.save()
            return redirect('professional_profile', user_form.username)


    user = get_user_model().objects.filter(username=username).first()
    if user:
        form = UserUpdateForm(instance=user)
        return render(
            request=request,
            template_name='users/perfilprofissional.html',
            context={'form': form}
            )
    return redirect('home')
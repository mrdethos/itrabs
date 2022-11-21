from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login
from django.contrib import messages
from .forms import UserRegistrationForm

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)        
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
    return render(request, 'users/login.html')
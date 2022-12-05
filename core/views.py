from django.shortcuts import render, redirect
from users.models import CustomUser

def home(request):
    return render(request, 'core/home.html')

def homespanish(request):
    return render(request, 'core/home-spanish.html')

def plans(request):
    if request.user.is_authenticated:
        return render(request, 'core/planos.html')
    return redirect('home')

def find_professionals(request):
    if request.user.is_authenticated:
        display_user = CustomUser.objects.all()
        return render(request, 'core/encontrarprofissionais.html', {
            'display_user': display_user,
        })
    return redirect('home')
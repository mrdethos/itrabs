from django.shortcuts import render, redirect

def home(request):
    return render(request, 'core/home.html')

def homespanish(request):
    return render(request, 'core/home-spanish.html')

def plans(request):
    return render(request, 'core/planos.html')

def find_professionals(request):
    return render(request, 'core/encontrarprofissionais.html')
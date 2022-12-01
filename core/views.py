from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def homespanish(request):
    return render(request, 'core/home-spanish.html')
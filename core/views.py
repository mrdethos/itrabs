from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def login(request):
    return render(request, 'core/login.html')

def signup(request):
    return render(request, 'core/signup.html')
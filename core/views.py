from django.shortcuts import render, redirect
from users.models import CustomUser
from django.db.models import Q

def home(request):
    if request.user.is_authenticated:
        user = request.user
        return redirect('customer_profile', user.username)
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

def search(request):
    if request.user.is_authenticated:
        search_data = request.POST.get('search_data')
        searched = CustomUser.objects.filter(Q(username__contains=search_data) |
                                             Q(languages__contains=search_data) |
                                             Q(email__contains=search_data) |
                                             Q(category__contains=search_data))
        return render(request, 'core/search.html', {
            'users': searched,
        })
    return redirect('home')
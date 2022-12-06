from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model, login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import *


def signup(request):
    if request.user.is_authenticated:
        user = request.user
        return redirect('customer_profile', user.username)
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('customer_profile', user.username)
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
        user = request.user
        return redirect('customer_profile', user.username)
    
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
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = request.user
            if 'update_right_info' in request.POST:
                form = UserUpdateFormRightInfo(request.POST, request.FILES, instance=user)
                if form.is_valid():
                    user_form = form.save()
                    return redirect('customer_profile', user_form.username)
            elif 'update_general_info' in request.POST:
                form = UserUpdateFormAboutGeneral(request.POST, request.FILES, instance=user)
                if form.is_valid():
                    user_form = form.save()
                    return redirect('customer_profile', user_form.username)
            elif 'update_looking_info' in request.POST:
                form = UserUpdateFormAboutLooking(request.POST, request.FILES, instance=user)
                if form.is_valid():
                    user_form = form.save()
                    return redirect('customer_profile', user_form.username)
            elif 'about_expectation' in request.POST:
                form = UserUpdateFormAboutExpectation(request.POST, request.FILES, instance=user)
                if form.is_valid():
                    user_form = form.save()
                    return redirect('customer_profile', user_form.username)
        user = get_user_model().objects.filter(username=username).first()
        if user:
            form_right_info = UserUpdateFormRightInfo(instance=user)
            form_general_info = UserUpdateFormAboutGeneral(instance=user)
            form_looking_info = UserUpdateFormAboutLooking(instance=user)
            form_expectation_info = UserUpdateFormAboutExpectation(instance=user)
            return render(
                request=request,
                template_name='users/perfilcontratante.html',
                context={
                    'form': form_right_info,
                    'form_general_info': form_general_info,
                    'form_looking_info': form_looking_info,
                    'form_expectation_info': form_expectation_info,
                })
        return redirect('customer_profile', user.username)
    return redirect('home')

def professional_profile(request, username):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = request.user
            if 'update_right_info' in request.POST:
                form = UserUpdateFormRightInfo(request.POST, request.FILES, instance=user)
                if form.is_valid():
                    user_form = form.save()
                    return redirect('professional_profile', user_form.username)
            elif 'update_professional_info' in request.POST:
                form = UserUpdateFormAboutProfessional(request.POST, request.FILES, instance=user)
                if form.is_valid():
                    user_form = form.save()
                    return redirect('professional_profile', user_form.username)
            elif 'update_professional_history_info' in request.POST:
                form = UserUpdateFormAboutProfessionalHistory(request.POST, request.FILES, instance=user)
                if form.is_valid():
                    user_form = form.save()
                    return redirect('professional_profile', user_form.username)
            elif 'update_advertisement_info' in request.POST:
                form = UserUpdateFormAboutAdvertisement(request.POST, request.FILES, instance=user)
                if form.is_valid():
                    user_form = form.save()
                    return redirect('professional_profile', user_form.username)

        user = get_user_model().objects.filter(username=username).first()
        if user:
            form = UserUpdateFormRightInfo(instance=user)
            form_professional_info = UserUpdateFormAboutProfessional(instance=user)
            form_professional_history = UserUpdateFormAboutProfessionalHistory(instance=user)
            form_advertisement = UserUpdateFormAboutAdvertisement(instance=user)
            return render(
                request=request,
                template_name='users/perfilprofissional.html',
                context={
                        'form': form,
                        'form_professional_info': form_professional_info,
                        'form_professional_history': form_professional_history,
                        'form_advertisement': form_advertisement,
                })
        return redirect('home')
    return redirect('home')
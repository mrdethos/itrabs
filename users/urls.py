from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('cprofile/<username>', views.customer_profile, name='customer_profile'),
    path('pprofile/<username>', views.professional_profile, name='professional_profile'),
]
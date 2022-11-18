from django.urls import path, include
from core import views
from core.views import home

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    #path('signup/', views.signup, name='signup'),
]

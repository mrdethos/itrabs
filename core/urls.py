from django.urls import path, include
from core import views
from core.views import home

urlpatterns = [
    path('', views.home, name='home'),
    path('es/', views.homespanish, name='homespanish'),
]

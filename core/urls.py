from django.urls import path, include
from core import views
from core.views import home

urlpatterns = [
    path('', views.home, name='home'),
    path('es/', views.homespanish, name='homespanish'),
    path('plans/', views.plans, name='plans'),
    path('find_professionals/', views.find_professionals, name='find_professionals'),
    path('search/', views.search, name='search'),
]

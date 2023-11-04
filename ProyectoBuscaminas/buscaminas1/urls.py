from django.urls import path
from buscaminas1 import views

urlpatterns = [
    path('', views.crea_tablero, name='crea_tablero'),
]

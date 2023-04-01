from django.urls import path
from . import views

urlpatterns = [
    path('', views.formulario2, name='formulario2'),
    path('calcular', views.calcular, name='calcular'),
]
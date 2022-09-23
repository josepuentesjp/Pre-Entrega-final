from xml.etree.ElementInclude import include
from django.urls import path
from website.views import *

urlpatterns = [
    path('', inicio),
    path('Categorias/', categorias),
    path('Tareas/', tareas),
    path('Trabajadores/', trabajadores),
]
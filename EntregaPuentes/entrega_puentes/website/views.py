from django.shortcuts import render
from django.http import HttpResponse
from website.models import *

# Create your views here.

def inicio(request):
    return render(request, 'website/home.html')

def categorias(request):
    return render(request, 'website/categories.html')

def tareas(request):
    return render(request, 'website/tasks.html')

def trabajadores(request):
    return render(request, 'website/workers.html')
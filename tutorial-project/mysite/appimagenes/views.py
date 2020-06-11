from django.shortcuts import render
from django.http import HttpResponse

from .models import ImagenesModel

def student_show(request):
    imagenes = ImagenesModel.objects.all()
    imagenes_primera = imagenes[0].imagen
    imagenes_resto = imagenes[1:len(imagenes)]
    num = len(imagenes)
    vector = []
    for i in range(num):
        vector.append(i)
    return render(request, 'appimagenes/carrusel_prueba.html', {'imagenes':imagenes ,'imagenesprimera': imagenes_primera,'imagenesresto': imagenes_resto, 'num': num, 'vector': vector})

def webpage_show(request):
    imagenes = ImagenesModel.objects.all()
    imagenes_primera = imagenes[0].imagen
    imagenes_resto = imagenes[1:len(imagenes)]
    num = len(imagenes)
    vector = []
    for i in range(num):
        vector.append(i)
    return render(request, 'appimagenes/carrusel_pagina.html', {'imagenes':imagenes ,'imagenesprimera': imagenes_primera,'imagenesresto': imagenes_resto, 'num': num, 'vector': vector})

# Create your views here.

from django.shortcuts import render

from . import peticion

def home (request):
    return render(request, 'clima.html', peticion.getInfo())

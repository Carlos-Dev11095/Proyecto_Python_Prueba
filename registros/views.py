from django.shortcuts import render
from .models import Alumnos
# Create your views here.
def registros(request):
    alumnos=Alumnos.objects.all()
    return render(request,"registros/principal.html",{'alumnos':alumnos})
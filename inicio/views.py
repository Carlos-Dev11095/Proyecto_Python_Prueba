from django.shortcuts import render, HttpResponse

# Create your views here.

def formulario(request):
    return render(request,"inicio/formulario.html")

def ejemplo(request):
    return render(request,"inicio/ejemplo.html")

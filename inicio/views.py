from django.shortcuts import render,HttpResponse

# Create your views here.
def principal(request):
    return render(request,'inicio/principal.html')

def formulario(request):
    return render(request,'inicio/formulario.html')

def contacto(request):
    return render(request,"inicio/contacto.html")
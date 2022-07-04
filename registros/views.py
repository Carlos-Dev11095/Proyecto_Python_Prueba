from django.shortcuts import render
from .models import Alumnos
from .forms import ComentarioContactoForm

# Create your views here.

def registros(request):
    alumnos=Alumnos.objects.all()
    #all recupera todos los objetos del modelo (registros de la tabla alumnos)
    return render(request,"registros/principal.html",{'alumnos':alumnos})
#Indicamos el lugar donde se renderizará el resultado de esta vista
# y enviamos la lista de alumnos recuparados

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid(): #si los datos recibidos son correctos
            form.save() #Inserta
            return render(request,'registros/contacto.html')
    form = ComentarioContactoForm()
    #Si algo sale mal se reenvian al formulario losdatos ingresados
    return render(request,'registros/contacto.html',{'form':form})

def contacto(request):
    return render(request,"registros/contacto.html")
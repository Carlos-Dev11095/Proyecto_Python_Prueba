from django.shortcuts import render
from .models import Alumnos, Archivos
from .forms import AlumnoForms, ComentarioContactoForm, FormArchivos
from .models import ComentarioContacto
from django.shortcuts import get_object_or_404
import datetime
from django.contrib import messages
# Create your views here.

def registros(request):
    alumnos=Alumnos.objects.all()
    return render(request,"registros/principal.html",{'alumnos':alumnos})

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid(): #si los datos recibidos son correctos
            form.save() #Inserta
            comentarios=ComentarioContacto.objects.all()
            return render(request,'registros/consultarComentarios.html',{'comentarios':comentarios})
    form = ComentarioContactoForm()
    #Si algo sale mal se reenvian al formulario losdatos ingresados
    return render(request,'registros/contacto.html',{'form':form})

def contacto(request):
    return render(request,"registros/contacto.html")


def ComentariosContacto(request):
    comentarios=ComentarioContacto.objects.all()
    return render(request,'registros/consultarComentarios.html',{'comentarios':comentarios})



def ConfirmeliminarComentarioContacto(request,id, confirmacion='registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method == 'POST':
        comentario.delete()
        comentarios=ComentarioContacto.objects.all()
        return render(request,'registros/consultarComentarios.html',{'comentarios':comentarios})
    return render(request, confirmacion,{'object':comentario})


def consultarComentarioContacto(request,id):
    comentario = ComentarioContacto.objects.get(id=id)
    return render(request,'registros/editarComentario.html',{'comentario':comentario})

def editarComentarioContacto(request,id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = ComentarioContactoForm(request.POST, instance=comentario)
    if form.is_valid():
        form.save()
        comentarios=ComentarioContacto.objects.all()
        return render(request,"registros/consultarComentarios.html",{'comentarios':comentarios})
    return render(request,'registros/editarComentario.html',{'comentario':comentario})


def eliminarAlumno(request,id, confirmacion='registros/confirmarEliminacionAlum.html'):
    alumno = get_object_or_404(Alumnos, id=id)
    if request.method == 'POST':
        alumno.delete()
        alumnos=Alumnos.objects.all()
        return render(request,'registros/principal.html',{'alumnos':alumnos})
    return render(request, confirmacion,{'object':alumno})


def consultarAlumno(request,id):
    alumno = Alumnos.objects.get(id=id)
    return render(request,'registros/editarAlumno.html',{'alumno':alumno})


def editarAlumnos(request,id):
    alumno = get_object_or_404(Alumnos, id=id)
    form = AlumnoForms(request.POST, instance=alumno)
    if form.is_valid():
        form.save()
        alumnos=Alumnos.objects.all()
        return render(request,'registros/principal.html',{'alumnos':alumnos})
    return render(request,'registros/editarAlumno.html',{'alumno':alumno})

def consultar1(request):
    alumnos=Alumnos.objects.filter(carrera="TI")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar2(request):
    alumnos=Alumnos.objects.filter(carrera="TI").filter(turno="Matutino")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar3(request):
    alumnos=Alumnos.objects.all().only("matricula","nombre","carrera","turno","imagen")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar4(request):
    alumnos=Alumnos.objects.filter(turno__contains="Vespertino")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar5(request):
    alumnos=Alumnos.objects.filter(nombre__in=["Juan","Ana"])
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar6(request):
    fechaInicio= datetime.date(2022,7,1)
    fechaFin= datetime.date(2022,7,13)
    alumnos=Alumnos.objects.filter(created__range=(fechaInicio,fechaFin))
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar7(request):
    alumnos=Alumnos.objects.filter(comentario__coment__contains="hola")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            titulo = request.POST['titulo']
            descripcion=request.POST['descripcion']
            archivo=request.FILES['archivo']
            insert= Archivos(titulo=titulo,descripcion=descripcion,archivo=archivo)
            insert.save()
            return render(request,'registros/archivos.html')
        else:
          messages.error(request, 'Error al procesar el formulario')
    else:
        return render(request,'registros/archivos.html',{'archivos':Archivos})

def consultasSQL(request):
    alumnos=Alumnos.objects.raw('SELECT id, matricula,nombre,carrera,turno,imagen FROM registros_alumnos WHERE carrera="TI" ORDER BY turno DESC')
    return render(request, 'registros/consultas.html',{'alumnos':alumnos})

def seguridad(request):
    return render(request,"registros/seguridad.html")
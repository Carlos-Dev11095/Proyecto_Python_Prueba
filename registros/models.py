from msilib.schema import Class
from pydoc import describe
from tabnanny import verbose
from turtle import update
from venv import create
from django.db import models
from ckeditor.fields import RichTextField

class Alumnos(models.Model): #Define la estructura de nuestra tabla
    id = models.AutoField(primary_key=True,verbose_name="id")
    matricula = models.CharField(max_length=12,verbose_name="Matrícula") #texto corto
    nombre = models.TextField() #Texto largo
    carrera = models.TextField()
    turno = models.CharField(max_length=10)
    imagen = models.ImageField(null=True,upload_to="fotos",verbose_name="Fotografía")
    created = models.DateField(auto_now_add=True) #Fecha y tiempo
    updated = models.DateField(auto_now_add=True) #Fecha y tiempo

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"
        ordering = ["-created"]
        #El - indica que se ordena del más reciente al mas viejo
    
    def __str__(self):
        return self.nombre
        #Indica que se mostrará el nombre como valor de la tabla

class Comentario(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    alumno = models.ForeignKey(Alumnos, on_delete=models.CASCADE,verbose_name="Alumno")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Registrado")
    coment = RichTextField(verbose_name="Comentario")

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ["-created"]
        #El - indica que se ordena del más reciente al mas viejo
    
    def __str__(self):
        return self.coment	

class ComentarioContacto(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    usuario = models.TextField(verbose_name="Alumno")
    mensaje = models.TextField(verbose_name="Comentario")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Registrado")

    class Meta:
        verbose_name = "Comentario Contacto"
        verbose_name_plural = "Comentarios Contactos"
        ordering = ["-created"]
        #El - indica que se ordena del más reciente al mas viejo
    
    def __str__(self):
        return self.mensaje

class Archivos(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    titulo= models.CharField(max_length=100,null=True,verbose_name="Titulo")
    descripcion = models.TextField(null=True,verbose_name="Descripcion")
    archivo = models.FileField(upload_to="archivos", null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Archivo"
        verbose_name_plural = "Archivos"
        ordering = ["-created"]

    def __str__(self):
        return self.titulo


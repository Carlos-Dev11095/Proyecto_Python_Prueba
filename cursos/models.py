from msilib.schema import Class
from tabnanny import verbose
from django.db import models

# Create your models here.

class Cursos(models.Model): #Define la estructura de nuestra tabla
    idcurso = models.SmallIntegerField(primary_key=True,verbose_name="Clave Curso") #principal auto
    nombre = models.TextField(max_length=30,verbose_name="Nombre del Curso") #Texto largo limitado
    descripcion = models.TextField(verbose_name="Descripción del Curso") #Texto largo
    activo = models.BooleanField(verbose_name="Estatus del Curso") #Booleano
    duracion = models.PositiveSmallIntegerField(verbose_name="Duración del Curso") #Int pequeño
    created = models.DateField(auto_now_add=True) 
    updated = models.DateField(auto_now_add=True) 

    class Meta:
        verbose_name = "curso"
        verbose_name_plural = "cursos"
        ordering = ["-created"]
        #El - Ordenado del más reciente a más nuevo
    
    def __str__(self):
        return self.nombre
        #Mostrado por nombre
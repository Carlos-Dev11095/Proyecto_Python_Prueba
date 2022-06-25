from msilib.schema import Class
from tabnanny import verbose
from django.db import models

class Alumnos(models.Model): #Define la estructura de nuestra tabla
    matricula = models.CharField(max_length=12,verbose_name="Mat") #texto corto
    nombre = models.TextField() #Texto largo
    carrera = models.TextField()
    turno = models.TextField(max_length=10)
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



from django.db import models

# Create your models here.

class alumnos(models.Model):#define la estructura de nuestra tabla
    matricula= models.CharField(max_length=12) #texto corto
    nombre = models.TextField()#texto largo
    carrera = models.TextField()
    turno = models.CharField(max_length=10) 
    created = models.DateField(auto_now_add=True) #fecha y tiempo
    update = models.DateField(auto_now_add=True)
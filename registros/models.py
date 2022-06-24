from django.db import models

# Create your models here.

class alumnos(models.Model):#define la estructura de nuestra tabla
    matricula= models.CharField(max_length=12,verbose_name="Mat") #texto corto
    nombre = models.TextField()#texto largo
    carrera = models.TextField()
    turno = models.CharField(max_length=10)
    created = models.DateField(auto_now_add=True) #fecha y tiempo
    update = models.DateField(auto_now_add=True)
    
class Meta:
    verbose_name = "Alumno"
    verbose_name_plural = "Alumnos"
    ordering = ["-created"]
#el menos indica que se ordenara del más reciente al mas viejo
        
def __str__(self):
    return self.nombre
#Indica que se mostrára el nombre como valor en la tabla
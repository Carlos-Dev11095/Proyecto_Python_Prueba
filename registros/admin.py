from django.contrib import admin
from registros.models import Alumnos
from .models import Comentario, ComentarioContacto

# Register your models here.
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('matricula', 'nombre', 'carrera','turno')
    search_fields = ('matricula','nombre','carrera','turno')
    date_hierarchy = 'created'
    list_filter = ('carrera','turno')
admin.site.register(Alumnos,AdministrarModelo)

class AdministrarComentarios(admin.ModelAdmin):
    list_display = ('id', 'coment')
    search_fields = ('id', 'coment')
    date_hierarchy = 'created'
    readondly_fields = ('created','id')
admin.site.register(Comentario,AdministrarComentarios)

class AdministrarComentariosContactos(admin.ModelAdmin):
    list_display = ('id', 'mensaje')
    search_fields = ('id', 'mensaje')
    date_hierarchy = 'created'
    readondly_fields = ('created','id')
admin.site.register(ComentarioContacto,AdministrarComentariosContactos)
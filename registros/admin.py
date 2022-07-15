from django.contrib import admin
from registros.models import Alumnos
from .models import Comentario, ComentarioContacto
from .models import Archivos

# Register your models here.


class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('matricula', 'nombre', 'carrera', 'turno','created')
    search_fields = ('matricula', 'nombre', 'carrera', 'turno')
    date_hierarchy = 'created'
    list_filter = ('carrera', 'turno')

    def get_readonly_fields(self, request, obj=None):
       if request.user.groups.filter(name="Usuarios").exists():
            return('matricula', 'carrera', 'turno')
       else:
            return ('created', 'updated')

admin.site.register(Alumnos, AdministrarModelo)

class AdministrarComentarios(admin.ModelAdmin):
    list_display = ('id', 'coment')
    search_fields = ('id', 'coment')
    date_hierarchy = 'created'
    readondly_fields = ('created', 'id')

admin.site.register(Comentario, AdministrarComentarios)


class AdministrarComentariosContactos(admin.ModelAdmin):
    list_display = ('id', 'mensaje')
    search_fields = ('id', 'mensaje')
    date_hierarchy = 'created'
    readondly_fields = ('created', 'id')
admin.site.register(ComentarioContacto, AdministrarComentariosContactos)

class AdminArchivos(admin.ModelAdmin):
    list_display = ('id', 'archivo')
    search_fields = ('id', 'archivo')
    date_hierarchy = 'created'
    readondly_fields = ('created', 'id')
admin.site.register(Archivos, AdminArchivos)
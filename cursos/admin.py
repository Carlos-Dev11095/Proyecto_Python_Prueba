from django.contrib import admin

from cursos.models import Cursos

# Register your models here.
class AdministrarModeloCursos(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Cursos,AdministrarModeloCursos)
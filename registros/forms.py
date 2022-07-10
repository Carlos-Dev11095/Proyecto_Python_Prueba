from django import forms
from .models import Alumnos, ComentarioContacto

class ComentarioContactoForm (forms.ModelForm):
    class Meta:
        model = ComentarioContacto
        fields = ['usuario', 'mensaje']

class AlumnoForms (forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = ['nombre', 'carrera']
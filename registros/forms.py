from pydoc import describe
from django import forms
from .models import Alumnos, ComentarioContacto, Archivos
from django.forms import ModelForm, ClearableFileInput 

class ComentarioContactoForm (forms.ModelForm):
    class Meta:
        model = ComentarioContacto
        fields = ['usuario', 'mensaje']

class AlumnoForms (forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = ['nombre', 'carrera']

class CustomClearableFileInput(ClearableFileInput):
    template_with_clear = '<br> <label for="%(clear_checkbox_id)s">%clear_checkbox_label)s</label>%(clear)s'

class FormArchivos(ModelForm):
    class Meta:
        model = Archivos
        fields =('titulo', 'descripcion', 'archivo')
        Widgets = {
            'archivo': CustomClearableFileInput
        }


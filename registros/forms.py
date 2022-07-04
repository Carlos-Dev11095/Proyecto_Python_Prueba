from django import forms
from .models import ComentarioContacto

class ComentarioContactoForm (forms.ModelForm):
    class Meta:
        model = ComentarioContacto
        fields = ['usuario', 'mensaje']
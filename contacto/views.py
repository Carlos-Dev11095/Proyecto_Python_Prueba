from django.shortcuts import render,HttpResponse

menu="""
<a href="/"><h2>Inicio</h2></a>"""

# Create your views here.
def contacto(request):
    contenido="""<h2>Contacto</h2>
    <p>Nombre: <input type="text" name="nombre"></p>
    <p>Mensaje:</p><p><textarea cols="50" rows="10"></textarea></p>
    <p><input type="Button" name="Enviar" value="Enviar"/></p>"""
    return HttpResponse(menu+contenido)

from django.shortcuts import render,HttpResponse

menu="""<h2>
<a href="/">Inicio</a>
 <a href="/contacto">Contactanos</a></h2>"""

# Create your views here.
def principal(request):
    contenido="<h1>HOLA DJANGO</h1>"
    return HttpResponse(menu+contenido)
"""prueba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicio import views
from django.conf import settings 
#permite acceder a las variables MEDIA_URL y MEDIA_ROOT que almacenan la ubicación de nuestras imagenes
from registros import views as views_registros
#Importamos la nueva vista de app registros para poder asignar las rutas de acceso a sus vista


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views_registros.registros, name="Principal"),
    path('contacto/',views_registros.contacto, name ="Contacto"),
    path('formulario/',views.formulario, name ="Formulario"),
    path('ejemplo/',views.ejemplo, name ="Ejemplo"),
    path('registrar/',views_registros.registrar, name ="Registrar"),
    path('comentarios/',views_registros.ComentariosContacto, name ="consultarComentarios"),
    path('registros/',views_registros.registros, name ="consultarAlumnos"),
    path('eliminarComentario/<int:id>/',views_registros.ConfirmeliminarComentarioContacto,name ="Eliminar"),
    path('eliminarAlumno/<int:id>/',views_registros.eliminarAlumno,name ="EliminarAlumno"),

    path('editarComentario/<int:id>/',views_registros.consultarComentarioContacto,name ="consultarComentario"),
    path('editarComentarioContacto/<int:id>/',views_registros.editarComentarioContacto,name ="Editar"),

    path('editarAlumno/<int:id>/',views_registros.consultarAlumno,name ="consultarAlumno"),
    path('guadarAlumnos/<int:id>/',views_registros.editarAlumnos,name ="EditarAlumno"),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
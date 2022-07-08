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
from registros import views as views_registros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views_registros.registros, name="Principal"),
    path('contacto/', views_registros.contacto, name="Contacto"),
    path('formulario/', views.formulario, name="Formulario"),
    path('ejemplo/', views.ejemplo, name="Ejemplo"),
    path('registrar/', views_registros.registrar, name="Registrar"),
    path('consultaComentarios/', views_registros.ComentariosContacto, name="consultaComentarios"),
    path('ConfirmeliminarComentario/<int:id>/',views_registros.ConfirmeliminarComentarioContacto,name ="Eliminar"),
    path('ConfirmeditarComentario/',views_registros.ConfirmeditarComentarioContacto,name ="Editar"),
    
]

if settings.DEBUG:
    from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)

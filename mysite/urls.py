"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('honda/', views.honda, name='honda'),
    path('hondaDetalle/<int:id>', views.honda_detalle, name='hondaDetalle'),
    path('hondaEdicion/<int:id>', views.honda_edicion, name='hondaEdicion'),
    path('hondaEliminar/<int:id>/eliminar', views.honda_eliminar, name='hondaEliminar'),
    path('bajaj/', views.bajaj, name='bajaj'),
    path('bajajDetalle/<int:id>', views.bajaj_detalle, name='bajajDetalle'),
    path('bajajEdicion/<int:id>', views.bajaj_edicion, name='bajajEdicion'),
    path('bajajEliminar/<int:id>/eliminar', views.bajaj_eliminar, name='bajajEliminar'),
    path('yamaha/', views.yamaha, name='yamaha'),
    path('yamahaDetalle/<int:id>', views.yamaha_detalle, name='yamahaDetalle'),
    path('yamahaEdicion/<int:id>', views.yamaha_edicion, name='yamahaEdicion'),
    path('yamahaEliminar/<int:id>/eliminar', views.yamaha_eliminar, name='yamahaEliminar'),
    path('ktm/', views.ktm, name='ktm'),
    path('ktmDetalle/<int:id>', views.ktm_detalle, name='ktmDetalle'),
    path('ktmEdicion/<int:id>', views.ktm_edicion, name='ktmEdicion'),
    path('ktmEliminar/<int:id>/eliminar', views.ktm_eliminar, name='ktmEliminar'),
    path('bmw/', views.bmw, name='bmw'),
    path('bmwDetalle/<int:id>', views.bmw_detalle, name='bmwDetalle'),
    path('bmwEdicion/<int:id>', views.bmw_edicion, name='bmwEdicion'),
    path('bmwEliminar/<int:id>/eliminar', views.bmw_eliminar, name='bmwEliminar'),
    path('otros/', views.otros, name='otros'),
    path('otrosDetalle/<int:id>', views.otro_detalle, name='otroDetalle'),
    path('otrosEdicion/<int:id>', views.otros_edicion, name='otrosEdicion'),
    path('otrosEliminar/<int:id>/eliminar', views.otros_eliminar, name='otrosEliminar'),
    path('conocenos/', views.conocenos, name='conocenos'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('iniciarsesion/', views.iniciarsesion, name='iniciarsesion'),
    path('perfil/', views.perfil, name='perfil'),
    path('cerrarsesion/', views.cerrarsesion, name='cerrarsesion'),
    path('subirpublicacion/', views.subirpublicacion, name="subirpublicacion"),
    path('comentario/<str:marca>/<int:id>', views.comentario, name="comentario"),
    path('comentarioEditar/<str:marca>/<int:moto_id>/<int:id>', views.comentarioeditar, name="comentarioEditar"),
    path('ComentarioEliminar/<str:marca>/<int:moto_id>/<int:id>/eliminar', views.comentarioeliminar, name='comentarioEliminar'),
]

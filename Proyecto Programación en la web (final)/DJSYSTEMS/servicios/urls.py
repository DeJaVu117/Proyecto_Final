from django.urls import path

from . import views

urlpatterns = [
    #ruta, vista, nombre interno
    path('gestion/',views.GestionServicio, name='gestion_servicio'),
    path('agregar/',views.AgregarServicio, name='agregar_servicio'),
    path('detalle/<id>/',views.VerServicio, name='ver_servicio'),
    path('editar/<id>/',views.EditarServicio, name='editar_servicio'),
    path('borrar/<id>/',views.BorrarServicio, name='borrar_servicio')
]
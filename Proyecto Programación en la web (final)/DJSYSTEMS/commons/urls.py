from django.urls import path

from . import views

urlpatterns = [
    #ruta, vista, nombre interno
    path('',views.index, name='index'),
    path('registro',views.registro,name='registro'),
    path('contacto/',views.contacto, name='contacto'),
     path('servicio/',views.servicio_view, name='servicio')
    
    
]
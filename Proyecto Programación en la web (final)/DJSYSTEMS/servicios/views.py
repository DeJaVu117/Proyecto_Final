from django.shortcuts import redirect,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from datetime import datetime

from .forms import ServicioForm
from .models import Servicio


def VerServicio(request, id):
          
    obj = get_object_or_404(Servicio, id=id)
    
    context = {'servicio':Servicio}
    #Obtener el template
    template = loader.get_template("VerServicio.html")
    return HttpResponse(template.render(context,request))

# Vista principal de Gestión de Productos
def GestionServicio(request):
    #Consultar productos
    servicios_list = Servicio.objects.all()
    #Configurar paginación cada 10 productos
    paginator = Paginator(servicios_list, 10)

    #Obtener página
    page_number = request.GET.get('page',0)
    page_obj = paginator.get_page(page_number)

    #Obtener el template
    template = loader.get_template("GestionServicio.html")
    #Agregar el contexto
    context = {"page_obj": page_obj}
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))

# Vista para crear productos
def AgregarServicio(request):
    #Obtener el template
    template = loader.get_template("AgregarServicio.html")
    #Generar Formulario
    if request.method == "POST":
        form = ServicioForm(request.POST or None, request.FILES)
        if form.is_valid():
            #obtener datos del formulario
            servicio_nuevo = form.save(commit=False)
            #Asignar fecha de creación
            servicio_nuevo.fecha_creacion = datetime.now()
            #Guardar Producto
            servicio_nuevo.save()
            return redirect('gestion_servicio')
    else:
        form = ServicioForm()
    #Crear contexto
    context = {}
    context['form'] = form
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))

# Vista de Productos
def EditarServicio(request,id):
    #Obtener el template
    template = loader.get_template("EditarServicio.html")
    #Buscar Producto
    obj = get_object_or_404(Servicio, id = id)
    #formulario que contiene la instancia
    form = ServicioForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('gestion_servicio')   
    #Agregar el contexto
    context = {}
    context['form'] = form
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))

# Vista de Productos
def BorrarServicio(request,id):
    #Obtener el template
    template = loader.get_template("BorrarServicio.html")
    #Buscar el producto
    obj = get_object_or_404(Servicio, id = id)
    if request.method == "POST":
        obj.delete()
        return redirect('gestion_servicio')
    #Agregar el contexto
    context = {}
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))
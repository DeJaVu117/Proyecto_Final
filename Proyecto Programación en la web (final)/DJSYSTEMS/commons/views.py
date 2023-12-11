

# Create your views here.
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login
from django.contrib import messages

from .forms import NewUserForm

# Create your views here.
def index(request):
    template = loader.get_template("index.html")
    context = {}
    return HttpResponse(template.render(context,request))

def registro(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request, "Registro Exitoso")
            return redirect('index')
        messages.error(request,"No fue posible el Registro. Información Invalida")
    form = NewUserForm()
    context = {"register_form":form}
    template = loader.get_template("register.html")
    return HttpResponse(template.render(context,request))

def contacto(request):
    template = loader.get_template("contacto.html")
    context = {}
    return HttpResponse(template.render(context,request))

def servicio_view(request):
    template = loader.get_template("servicio.html")
    context = {}
    return HttpResponse(template.render(context,request))    
    
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Inmuebles
from .forms import InmueblesForm
# Create your views here.

#Acceso a Inicio de la Pagina
def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')
#Acceso a Inmuebles y Crear un Inmueble
def inmuebles(request):
    inmuebles = Inmuebles.objects.all()    
    return render(request, 'inmuebles/index.html', {'inmuebles': inmuebles})

def crear(request):
    formulario = InmueblesForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('inmuebles')
    return render(request, 'inmuebles/crear.html', {'formulario': formulario})

def editar(request, id):
    inmueble = Inmuebles.objects.get(id=id)
    formulario = InmueblesForm(request.POST or None, request.FILES or None, instance=inmueble)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('inmuebles')
    return render(request, 'inmuebles/editar.html', {'formulario':formulario})

def borrar(request, id):
    inmueble = Inmuebles.objects.get(id=id)
    inmueble.delete()
    return redirect('inmuebles')


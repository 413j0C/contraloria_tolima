from django.shortcuts import redirect, render
from .forms import TipoActivoForm, SoftwareForm,HardwareForm
from django.contrib.auth.decorators import login_required
from .models import * 
from django.contrib import messages
from django.http.response import HttpResponse, JsonResponse

# Create your views here.

@login_required(login_url='inicio')
def registrar_activo(request):
    titulo="Registrar activo"
    form= TipoActivoForm()
    activos= TipoActivo.objects.all
    context={
        'titulo':titulo,
        'form': form,
        'activos':activos,   
    }  
    if request.method == 'POST':  
        form = TipoActivoForm(request.POST)
        activo = form.save(commit=False)
        activo.save()
        return render(request, 'activos/activo.html',context)
    else:
        return render(request, 'activos/activo.html',context)
    
    
def formulario(request, pk):
    activo= TipoActivo.objects.get(id=pk)
    titulo="Registrar activo"
    form= HardwareForm()
    form2=HardwareForm()
    context={
        'titulo':titulo,  
        'form2': form2,
        'activo': activo,
        'form': form,
    }  
    return render (request, 'activos/formulario.html' ,context)



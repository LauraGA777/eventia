from django.shortcuts import render, redirect
from django.contrib import messages
from activities.models import Activity
from . forms import ActivityForm

# Create your views here.

#Create 
def activities(request):
    form = ActivityForm(request.POST or None)
    activities = Activity.objects.all()
    if form.is_valid() and request.method == 'POST':
        try:
            form.save()
            messages.success(request,'Evento ingresado con exito!')
            return redirect('activities')
        except:
            messages.error(request, 'Ocurrio un error al registrar el evento')
            return redirect('activities')
    return render(request,'activities/index.html',{'form' : form, 'activities': activities})

#Read
def activities_read(request, id):
    try:
        activities = Activity.objects.get(id=id)
    except activities.DoesNotExist:
        messages.error(request,'El evento no existe')
    return render(request, 'activities/detail.html', {'activities': activities})

#Update
def activities_update(request, id):
    activities = Activity.objects.get(id=id)
    form = ActivityForm(request.POST or None, instance=activities)
    if form.is_valid() and request.method == 'POST':
        try:
            form.save()
            messages.success(request, 'Evento actualizado con éxito!')
            return redirect('activities')
        except:
            messages.error(request, 'Ocurrió un error al actualizar el evento')
            return redirect('activities')
    return render(request, 'activities/edit.html', {'form' : form})

#Delete
def activities_delete(request, id):
    activities = Activity.objects.get(id=id)
    try:
        activities.delete()
        messages.success(request,'Evento eliminado con exito')
        return redirect('activities')
    except:
        messages.error(request, 'Ocurrio un error al eliminar el evento')
        return redirect('activities')

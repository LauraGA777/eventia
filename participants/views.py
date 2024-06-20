from django.shortcuts import render, redirect
from django.contrib import messages
from participants.models import Participant
from . forms import ParticipantForm

# Create your views here.

#Create
def participants(request):
    form = ParticipantForm(request.POST or None)
    participants = Participant.objects.all()
    if form.is_valid() and request.method == 'POST':
        try:
            form.save()
            messages.success(request,'Participante registrado con exito')
            return redirect('participants')
        except:
            messages.error(request, 'Ocurrio un error al registrar el participante')
            return redirect('participants')
    return render(request,"participants/index.html",{'form' : form, 'participants' : participants})

#Read
def participants_read(request, id):
    try:
        participants = Participant.objects.get(id=id)
    except participants.DoesNotExist:
        messages.error(request,'Ocurrio un error')
    return render(request,"participants/detail.html",{'participants' : participants})

#Update
def participants_update(request, id):
    participants = Participant.objects.get(id=id)
    form = ParticipantForm(request.POST or None, instance=participants)
    if form.is_valid() and request.method == 'POST':
        try:
            form.save()
            messages.success(request,'Participante editado con exito')
            return redirect('participants')
        except:
            messages.error(request, 'Ocurrio un error al editar el participante')
            return redirect('participants')      
    return render(request, 'participants/edit.html', {'form' : form})

#Delete
def participants_delete(request, id):
    participants = Participant.objects.get(id=id)
    try:
        participants.delete()
        messages.success(request,'Participante eliminado con exito')
        return redirect('participants')
    except:
        messages.error(request, 'Ocurrio un error al eliminar el participante')
        return redirect('participants')

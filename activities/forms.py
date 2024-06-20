from django import forms
from activities.models import Activity

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'
        labels = {
            'name': 'Nombre del evento',
            'description': 'Descripción del evento',
            'date': 'Fecha del evento',
            'time':  'Hora del evento',
            'location': 'Ubicación del evento',
            'participant' : 'Participantes',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ingrese el nombre del evento'}),
            'description': forms.Textarea(attrs={'placeholder': 'Ingrese una descripción del evento'}),
            'date': forms.DateInput(attrs={'placeholder': 'Seleccione la fecha del evento', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'placeholder': 'Seleccione la hora del evento', 'type': 'time'}),
            'location': forms.TextInput(attrs={'placeholder': 'Ingrese la ubicación del evento'})
        }